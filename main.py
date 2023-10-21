""""
https://pillow.readthedocs.io/en/stable/reference/index.html
"""
from PIL import Image, ImageDraw, ImageColor


OUTPUT_FOLDER = './Output/'
TITLE = 'Circles'
COLORS = ["black"]
DPI = 300
WIDTH, HEIGHT = int(12 * DPI), int(12 * DPI)
SPACING = int(1.5 * DPI)


def draw_circles(canvas, radius, num_cols, page_width):

    page_height = page_width
    spacing = page_width // num_cols
    circle_color = 'black'

    for y_center in range(0, page_width + 1, spacing):
        for x_center in range(0, page_height + 1, spacing):
            x0 = x_center - radius
            x1 = x_center + radius
            y0 = y_center - radius
            y1 = y_center + radius

            canvas.ellipse([(x0, y0), (x1, y1)], fill=ImageColor.getrgb(circle_color))

    # Even rows
    for y_center in range(spacing // 2, page_width + 1, spacing):
        for x_center in range(spacing // 2, page_height + 1, spacing):
            x0 = x_center - radius
            x1 = x_center + radius
            y0 = y_center - radius
            y1 = y_center + radius

            canvas.ellipse([(x0, y0), (x1, y1)], fill=ImageColor.getrgb(circle_color))


def create_document():
    pass


if __name__ == '__main__':

    for radius in range(50, 200, 25):
        for num_cols in range(6, 13):
            circle_color = 'black'
            bg_color = 'white'
            filename = f"{OUTPUT_FOLDER}{TITLE}_radius{radius}_num_cols{num_cols}.jpg"
            img = Image.new('RGB', (WIDTH, HEIGHT), ImageColor.getrgb(bg_color))
            canvas = ImageDraw.Draw(img)

            # radius = 100
            # num_cols = 8
            page_width = 3600
            draw_circles(canvas, radius, num_cols, page_width)

            img.save(filename, "JPEG", dpi=(300, 300))
