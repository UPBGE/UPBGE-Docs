import bge
from bge import logic
from bge import texture as vt

# The default vertex shader, because we need one
#
VertexShader = """
#version 130
   void main()
   {
      gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
      gl_TexCoord[0] = gl_MultiTexCoord0;
   }

"""

# For use with RGB video stream: the pixel is directly usable
#
FragmentShader_R10l = """
    #version 130
    uniform sampler2D tex;
    // stereo = 1.0 if 2D image, =0.5 if 3D (left eye below, right eye above)
    uniform float stereo;
    // eye = 0.0 for the left eye, 0.5 for the right eye
    uniform float eye;

    void main(void)
    {
        vec4 color;
        float tx, ty;
        tx = gl_TexCoord[0].x;
        ty = eye+gl_TexCoord[0].y*stereo;
        color = texture(tex, vec2(tx,ty));
        color.a = 0.7;
        gl_FragColor = color;
    }
"""

# For use with YUV video stream
#
FragmentShader_2vuy = """
    #version 130
    uniform sampler2D tex;
    // stereo = 1.0 if 2D image, =0.5 if 3D (left eye below, right eye above)
    uniform float stereo;
    // eye = 0.0 for the left eye, 0.5 for the right eye
    uniform float eye;

    void main(void)
    {
        vec4 color;
        float tx, ty, width, Y, Cb, Cr;
        int px;
        tx = gl_TexCoord[0].x;
        ty = eye+gl_TexCoord[0].y*stereo;
        width = float(textureSize(tex, 0).x);
        color = texture(tex, vec2(tx, ty));
        px = int(floor(fract(tx*width)*2.0));
        switch (px) {
        case 0:
            Y = color.g;
            break;
        case 1:
            Y = color.a;
            break;
        }
        Y = (Y - 0.0625) * 1.168949772;
        Cb = (color.b - 0.0625) * 1.142857143 - 0.5;
        Cr = (color.r - 0.0625) * 1.142857143 - 0.5;
        color.r = Y + 1.5748 * Cr;
        color.g = Y - 0.1873 * Cb - 0.4681 * Cr;
        color.b = Y + 1.8556 * Cb;
        color.a = 0.7;
        gl_FragColor = color;
    }
"""

# For use with high resolution YUV
#
FragmentShader_v210 = """
    #version 130
    uniform sampler2D tex;
    // stereo = 1.0 if 2D image, =0.5 if 3D (left eye below, right eye above)
    uniform float stereo;
    // eye = 0.0 for the left eye, 0.5 for the right eye
    uniform float eye;

    void main(void)
    {
        vec4 color, color1, color2, color3;
        int px;
        float tx, ty, width, sx, dx, bx, Y, Cb, Cr;
        tx = gl_TexCoord[0].x;
        ty = eye+gl_TexCoord[0].y*stereo;
        width = float(textureSize(tex, 0).x);
        // to sample macro pixels (6 pixels in 4 words)
        sx = tx*width*0.25+0.01;
        // index of display pixel in the macro pixel 0..5
        px = int(floor(fract(sx)*6.0));
        // increment as we sample the macro pixel
        dx = 1.0/width;
        // base x coord of macro pixel
        bx = (floor(sx)+0.01)*dx*4.0;
        color = texture(tex, vec2(bx, ty));
        color1 = texture(tex, vec2(bx+dx, ty));
        color2 = texture(tex, vec2(bx+dx*2.0, ty));
        color3 = texture(tex, vec2(bx+dx*3.0, ty));
        switch (px) {
        case 0:
        case 1:
            Cb = color.b;
            Cr = color.r;
            break;
        case 2:
        case 3:
            Cb = color1.g;
            Cr = color2.b;
            break;
        default:
            Cb = color2.r;
            Cr = color3.g;
            break;
        }
        switch (px) {
        case 0:
            Y = color.g;
            break;
        case 1:
            Y = color1.b;
            break;
        case 2:
            Y = color1.r;
            break;
        case 3:
            Y = color2.g;
            break;
        case 4:
            Y = color3.b;
            break;
        default:
            Y = color3.r;
            break;
        }
        Y = (Y - 0.0625) * 1.168949772;
        Cb = (Cb - 0.0625) * 1.142857143 - 0.5;
        Cr = (Cr - 0.0625) * 1.142857143 - 0.5;
        color.r = Y + 1.5748 * Cr;
        color.g = Y - 0.1873 * Cb - 0.4681 * Cr;
        color.b = Y + 1.8556 * Cb;
        color.a = 0.7;
        gl_FragColor = color;
    }
"""

# The exhausitve list of pixel formats that are transferred as float texture
# Only use those for greater efficiency and compatiblity.
#
fg_shaders = {
    '2vuy'       :FragmentShader_2vuy,
    '8BitYUV'    :FragmentShader_2vuy,
    'v210'       :FragmentShader_v210,
    '10BitYUV'   :FragmentShader_v210,
    '8BitBGRA'   :FragmentShader_R10l,
    'BGRA'       :FragmentShader_R10l,
    '8BitARGB'   :FragmentShader_R10l,
    '10BitRGBXLE':FragmentShader_R10l,
    'R10l'       :FragmentShader_R10l
    }


#
# Helper function to attach a pixel shader to the material that receives the video frame.
#

def config_video(obj, format, pixel, is3D=False, mat=0, card=0):
    if pixel not in fg_shaders:
        raise('Unsuported shader')
    shader = obj.meshes[0].materials[mat].getShader()
    if shader is not None and not shader.isValid():
        shader.setSource(VertexShader, fg_shaders[pixel], True)
        shader.setSampler('tex', 0)
        shader.setUniformEyef("eye")
        shader.setUniform1f("stereo", 0.5 if is3D else 1.0)
    tex = vt.Texture(obj, mat)
    tex.source = vt.VideoDeckLink(format + "/" + pixel + ("/3D" if is3D else ""), card)
    print("frame rate: ", tex.source.framerate)
    tex.source.play()
    obj["video"] = tex

#
# Attach this function to an object that has a material with texture
# and call it once to initialize the object
#
def init(cont):
    # config_video(cont.owner, 'HD720p5994', '8BitBGRA')
    # config_video(cont.owner, 'HD720p5994', '8BitYUV')
    # config_video(cont.owner, 'pal ', '10BitYUV')
    config_video(cont.owner, 'pal ', '8BitYUV')


#
# To be called on every frame
#
def play(cont):
    obj = cont.owner
    video = obj.get("video")
    if video is not None:
        video.refresh(True)
