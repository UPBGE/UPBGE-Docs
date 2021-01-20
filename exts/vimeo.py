#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import division

import re
from docutils import nodes
from docutils.parsers.rst import directives, Directive

CONTROL_HEIGHT = 30

_re_size = re.compile("(\d+)(|%|px)$")
_re_aspect = re.compile("(\d+):(\d+)")


def get_size(d, key):
    if key not in d:
        return None
    m = _re_size.match(d[key])
    if not m:
        raise ValueError("invalid size %r" % d[key])
    return int(m.group(1)), m.group(2) or "px"


def css(d):
    return "; ".join(sorted("%s: %s" % kv for kv in d.items()))


class vimeo(nodes.General, nodes.Element):
    pass


def visit_vimeo_node(self, node):
    aspect = node["aspect"]
    width = node["width"]
    height = node["height"]

    if aspect is None:
        aspect = 16, 9

    if (height is None) and (width is not None) and (width[1] == "%"):
        style = {
            "padding-top": "%dpx" % CONTROL_HEIGHT,
            "padding-bottom": "%f%%" % (width[0] * aspect[1] / aspect[0]),
            "width": "%d%s" % width,
            "position": "relative",
        }
        self.body.append(self.starttag(node, "div", style=css(style)))
        style = {
            "position": "absolute",
            "top": "0",
            "left": "0",
            "width": "100%",
            "height": "100%",
            "border": "0",
        }
        attrs = {
            "src": "https://player.vimeo.com/video/%s" % node["id"],
            "style": css(style),
        }
        self.body.append(self.starttag(node, "iframe", **attrs))
        self.body.append("</iframe></div>")
    else:
        if width is None:
            if height is None:
                width = 560, "px"
            else:
                width = height[0] * aspect[0] / aspect[1], "px"
        if height is None:
            height = width[0] * aspect[1] / aspect[0], "px"
        style = {
            "width": "%d%s" % width,
            "height": "%d%s" % (height[0] + CONTROL_HEIGHT, height[1]),
            "border": "0",
        }
        attrs = {
            "src": "https://player.vimeo.com/video/%s" % node["id"],
            "style": css(style),
        }
        self.body.append(self.starttag(node, "iframe", **attrs))
        self.body.append("</iframe>")


def depart_vimeo_node(self, node):
    pass


def nop_node(self, node):
    pass


#Blender custom for not html builders
def process_vimeo_node(app, doctree, fromdocname):
    if app.builder.name != "html" and app.builder.name != "singlehtml":
        for node in doctree.traverse(vimeo):
            para = nodes.paragraph()
            t = "A video can be found at "
            intex = nodes.Text(t, t)
            para += intex

            href = "https://vimeo.com/%s" % node["id"]
            linknode = nodes.reference('', '', internal=False, refuri=href)
            innernode = nodes.inline('', href)
            linknode.append(innernode)
            para += linknode

            node.replace_self(para)


class Vimeo(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        "width": directives.unchanged,
        "height": directives.unchanged,
        "aspect": directives.unchanged,
    }

    def run(self):
        if "aspect" in self.options:
            aspect = self.options.get("aspect")
            m = _re_aspect.match(aspect)
            if m is None:
                raise ValueError("invalid aspect ratio %r" % aspect)
            aspect = tuple(int(x) for x in m.groups())
        else:
            aspect = None
        width = get_size(self.options, "width")
        height = get_size(self.options, "height")
        return [
            vimeo(
                id=self.arguments[0],
                aspect=aspect,
                width=width,
                height=height,
                )
             ]


def setup(app):
    app.add_node(
            vimeo,
            html=(visit_vimeo_node, depart_vimeo_node),
            latex=(nop_node, nop_node),
            text=(nop_node, nop_node),
            )
    app.add_directive("vimeo", Vimeo)
    #event listener: replace node if not html builder
    app.connect('doctree-resolved', process_vimeo_node)
    return {
        "parallel_read_safe": True,
    }
