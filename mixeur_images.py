import gradio as gr
from PIL import Image

def blend_images(img1, img2, alpha):
    img1 = img1.convert("RGBA")
    img2 = img2.convert("RGBA").resize(img1.size)
    blended = Image.blend(img1, img2, alpha)
    return blended

iface = gr.Interface(
    fn=blend_images,
    inputs=[
        gr.Image(type="pil", label="Image 1"),
        gr.Image(type="pil", label="Image 2"),
        gr.Slider(0, 1, value=0.5, label="Mix Ratio (alpha)")
    ],
    outputs=gr.Image(type="pil", label="Blended Image"),
    title="Mixeur d'Images Simple",
    description="Choisissez deux images et mixez-les avec un ratio."
)

iface.launch()
