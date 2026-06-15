from PyPDF2 import PdfMerger, PdfReader, PdfWriter

print("1. Merge PDFs")
print("2. Split PDF")

choice = int(input("Enter your choice: "))

if choice == 1:
    merger = PdfMerger()

    n = int(input("How many PDFs do you want to merge? "))

    for i in range(n):
        pdf = input(f"Enter PDF {i+1} file name: ")
        merger.append(pdf)

    output = input("Enter output file name: ")
    merger.write(output)
    merger.close()

    print("PDFs merged successfully!")

elif choice == 2:
    pdf = input("Enter PDF file name: ")
    page_no = int(input("Enter page number to extract: "))

    reader = PdfReader(pdf)
    writer = PdfWriter()

    writer.add_page(reader.pages[page_no - 1])

    output = input("Enter output file name: ")

    with open(output, "wb") as f:
        writer.write(f)

    print("PDF page extracted successfully!")

else:
    print("Invalid Choice!")