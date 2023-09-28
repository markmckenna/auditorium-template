from auditorium import Show

import numpy as np
import matplotlib.pyplot as plt

show = Show("Project Orca")

@show.slide
def title(ctx):
    """
    # Project Orca
    ## (AppleTV Everywhere for OTT)
    ### Mark McKenna (and friends)
    """

def overview(ctx):
    """
    ## Overview
    
    """

@show.slide
def my_slide(ctx):
    ctx.header("Header")
    ctx.markdown("""
        - Item 1
        - Item 2
        - Item 3
    """)

@show.slide
def slide2(ctx):
    """
    ## Static Markdown content
    Test
    """

@show.slide
def slide3(ctx):
    with ctx.columns(2, 3) as cl:
        ctx.markdown("left")
        cl.tab()
        ctx.markdown("right")

@show.slide
def slide4(ctx):
    input = ctx.text_input("input")
    ctx.markdown(f"Hello, {input}!")

@show.slide
def slide5(ctx):
    with ctx.animation(steps=10, time=0.33, loop=True) as anim:
        ctx.markdown("###" + ("."*anim.current))

@show.slide
def vertical(ctx):
    """Read more down"""

@vertical.slide
def vertical2(ctx):
    """Yay!"""

@show.slide
def slide7(ctx):
    with ctx.fragment():
        ctx.markdown("test")
    with ctx.fragment():
        ctx.markdown("test2")

@show.slide
def slide8(ctx):
    xg = np.random.RandomState(0)
    yg = np.random.RandomState(1)
    
    with ctx.animation(steps=60, time=0.5, loop=True) as anim:
        x = xg.uniform(size=anim.current * 50)
        y = yg.uniform(size=anim.current * 50)
        plt.scatter(x, y, s=3)
        plt.ylim(0, 1)
        plt.xlim(0, 1)

        ctx.pyplot(plt, fmt='png', height=350)