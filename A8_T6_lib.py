from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle

def drawSquare(PDwg: Drawing) -> None:
    print("Insert square")
    x = int(input("- Left edge position: "))
    y = int(input("- Top edge position: "))
    size = int(input("- Side length: "))
    fill_color = input("- Fill color: ")
    stroke_color = input("- Stroke color: ")
    square = Rect(insert=(x, y),
                  size=(size, size),
                  fill=fill_color,
                  stroke=stroke_color)
    PDwg.add(square)
    print()
    return None

def drawCircle(PDwg: Drawing) -> None:
    print("Insert circle")
    cx = int(input("- Center X coord: "))
    cy = int(input("- Center Y coord: "))
    r = int(input("- Radius: "))
    fill_color = input("- Fill color: ")
    stroke_color = input("- Stroke color: ")
    circle = Circle(center=(cx, cy),
                    r=r,
                    fill=fill_color,
                    stroke=stroke_color)
    PDwg.add(circle)
    print()
    return None

def saveSvg(PDwg: Drawing) -> None:
    filename = input("Insert filename: ")
    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ")
    if proceed.lower() != "y":
        print("Save aborted.\n")
        return None
    PDwg.saveas(filename, pretty=True, indent=2)
    print("Vector saved successfully!\n")
    return None