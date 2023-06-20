import sys
from shape import Shape
from circle import Circle
from ellipse import Ellipse
from rhombus import Rhombus


def load(file_name, shapes):
    error_count = 0
    processed_rows = 0

    try:
        print(f"\nProcessing {file_name}...")
        with open(file_name, "r") as file:
            lines = file.readlines()

            for line_number, line in enumerate(lines, start=1):
                line = line.strip()

                if not line:
                    continue

                processed_rows += 1
                words = line.split()

                try:
                    if words[0] == "shape":
                        shape = Shape()

                    elif words[0] == "circle":
                        radius = float(words[1])
                        shape = Circle(radius)

                        if radius <= 0:
                            raise ValueError(f"Invalid Circle on line {line_number} : {line}")

                    elif words[0] == "ellipse":
                        axis_a = float(words[1])
                        axis_b = float(words[2])

                        if axis_a <= 0 or axis_b <= 0:
                            raise ValueError(f"Invalid Ellipse on line {line_number}: {line}")

                        shape = Ellipse(axis_a, axis_b)

                    elif words[0] == "rhombus":
                        diagonal1 = float(words[1])
                        diagonal2 = float(words[2])
                        shape = Rhombus(diagonal1, diagonal2)

                        if diagonal1 <= 0 or diagonal2 <= 0:
                            raise ValueError(f"Invalid Ellipse on line {line_number}: {line}")

                    else:
                        raise ValueError(f"Invalid shape on line {line_number}: {line}")

                    shapes.append(shape)

                except (IndexError, ValueError) as error:
                    print(f"Error: {str(error)} on line {line_number}: {line}")
                    error_count += 1

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

    print(f"Processed {processed_rows} row(s), {len(shapes)} shape(s) added, {error_count} error(s).")


def toset(shapes):
    unique_shapes = []
    seen_shapes = []

    for shape in shapes:
        if shape not in seen_shapes:
            unique_shapes.append(shape)
            seen_shapes.append(shape)

    print("\nDuplicates successfully removed")
    return unique_shapes


def save(file_name, shapes):
    try:
        with open(file_name, "w") as file:
            for shape in shapes:
                file.write(str(shape) + "\n")
        print("\nDatabase saved successfully")
    except IOError:
        print("\nError: Unable to save the database to the file.")


def print_shapes(shapes):
    sorted_shapes = sorted(shapes, key=shapes.index)
    for shape in sorted_shapes:
        shape.print()


def summary(shapes):
    shape_counts = {}
    total_shapes = 0

    for shape in shapes:
        shape_name = shape.__class__.__name__
        shape_counts[shape_name] = shape_counts.get(shape_name, 0) + 1
        total_shapes += 1

    sorted_shapes = sorted(shape_counts.items())

    for i, (shape, count) in enumerate(sorted_shapes):
        if i == 3:
            continue
        plural_suffix = "(s)"
        if shape == "rhombus":
            plural_suffix = "(es)"
        print(f"{shape}{plural_suffix}: {count}")

    shape_counts["Shape"] = total_shapes
    print(f"Shape(s): {shape_counts['Shape']}")


def details(shapes):
    print("database:")
    shape_count = 0

    for shape in shapes:
        if isinstance(shape, Shape) and not isinstance(shape, Circle) and not isinstance(shape, Ellipse) and not isinstance(shape, Rhombus):
            print("shape")
            shape_count += 1

    for shape in shapes:
        if isinstance(shape, Circle):
            print(f"circle {shape.radius}")

    # Print Ellipses
    for shape in shapes:
        if isinstance(shape, Ellipse):
            print(f"ellipse {shape.a} {shape.b}")

    # Print Rhombuses
    for shape in shapes:
        if isinstance(shape, Rhombus):
            print(f"rhombus {shape.p} {shape.q}")


def quit(shapes):
    sys.exit()


def main():
    shapes = []

    while True:
        print("\nShape Database Menu\n~~~~~~~~~~~~~~~~~~~")
        print("1. LOAD file")
        print("2. TOSET")
        print("3. SAVE file")
        print("4. PRINT")
        print("5. SUMMARY")
        print("6. DETAILS")
        print("7. QUIT")

        choice = input("Select an operation (1-7): ")

        if choice == "1":
            file_name = input("\nEnter the file name: ")
            load(file_name, shapes)
        elif choice == "2":
            shapes = toset(shapes)
        elif choice == "3":
            file_name = input("\nEnter the file name: ")
            save(file_name, shapes)
        elif choice == "4":
            print_shapes(shapes)
        elif choice == "5":
            summary(shapes)
        elif choice == "6":
            details(shapes)
        elif choice == "7":
            print("\nProgram terminated. See you next time!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
