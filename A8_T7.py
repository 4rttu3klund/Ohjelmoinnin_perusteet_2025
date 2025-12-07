import math
import svgwrite
from svgwrite.shapes import Rect, Circle, Polygon

def drawSquare(dwg: svgwrite.Drawing) -> None:
    print("Insert square")
    x = int(input("- Left edge position: "))
    y = int(input("- Top edge position: "))
    side = int(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    dwg.add(Rect(insert=(x, y),
                 size=(side, side),
                 fill=fill,
                 stroke=stroke))
    print()
    return None

def drawCircle(dwg: svgwrite.Drawing) -> None:
    print("Insert circle")
    cx = int(input("- Center X coord: "))
    cy = int(input("- Center Y coord: "))
    r = int(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    dwg.add(Circle(center=(cx, cy),
                   r=r,
                   fill=fill,
                   stroke=stroke))
    print()
    return None

def drawHexagon(dwg: svgwrite.Drawing) -> None:
    print("Insert hexagon details:")
    cx = int(input("Middle point X: "))
    cy = int(input("Middle point Y: "))
    apothem = float(input("Apothem length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")
    R = apothem / math.cos(math.radians(30))
    anglesDeg = [ -60, 0, 60, 120, 180, 240 ]
    points = []
    for angle in anglesDeg:
        rad = math.radians(angle)
        x = cx + R * math.cos(rad)
        y = cy + R * math.sin(rad)
        points.append((round(x), round(y)))
    dwg.add(Polygon(points=points,
                    fill=fill,
                    stroke=stroke))
    print()
    return None

def saveSvg(dwg: svgwrite.Drawing) -> None:
    filename = input("Insert filename: ")
    print(f'Saving file to "{filename}"')
    confirm = input("Proceed (y/n)?: ").strip().lower()
    if confirm != "y":
        print("Save cancelled.\n")
        return None
    dwg.saveas(filename, pretty=True, indent=2)
    print("Vector saved successfully!\n")
    return None

def main() -> None:
    print("Program starting.")
    dwg = svgwrite.Drawing()
    while True:
        print("Options:")
        print("1 - Draw square")
        print("2 - Draw circle")
        print("3 - Draw hexagon")
        print("4 - Save svg")
        print("0 - Exit")
        choice = input("Your choice: ")
        if choice == "0":
            print("Exiting program.\n")
            break
        elif choice == "1":
            drawSquare(dwg)
        elif choice == "2":
            drawCircle(dwg)
        elif choice == "3":
            drawHexagon(dwg)
        elif choice == "4":
            saveSvg(dwg)
        else:
            print("Unknown option!\n")
    print("Program ending.")

if __name__ == "__main__":
    main()