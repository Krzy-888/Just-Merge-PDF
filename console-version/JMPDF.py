from pypdf import PdfWriter

def Just_Merge_PDF(in_PDFs, out_PDF):
    merger = PdfWriter()
    in_PDFs = in_PDFs.split(",")
    if in_PDFs[-1] == "Sort":
        in_PDFs = in_PDFs[0:len(in_PDFs)-1]
        in_PDFs.sort()
    for pdf in in_PDFs:
        merger.append(pdf)
    merger.write(out_PDF + ".pdf")

in_PDFs = input("Provide names of PDFs to merge separated by comma symbol,\nadd 'Sort' to sort PDFs by name:\t")
out_PDF = input("Provide name of output PDF:\t")

try:
    Just_Merge_PDF(in_PDFs, out_PDF)
except:
    print("Something went wrong!")