import streamlit as st
from manim import *

# Define your manim scene
class AnimatedScene(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        self.play(Create(circle))
        self.play(circle.animate.shift(2 * RIGHT))
        self.play(circle.animate.scale(2))
        self.play(circle.animate.set_color(RED))
        self.play(FadeOut(circle))

# Function to run the animation and display it in Streamlit
def display_animation():
    # Create the animation
    scene = AnimatedScene()

    # Save the animation to a file
    scene.render()

    # Display the video in Streamlit
    st.video("media/videos/animated_scene.mp4")

# Streamlit app layout
st.title("Manim Animation in Streamlit")
display_animation()
