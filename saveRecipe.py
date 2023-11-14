import fpdf
import os



def save(recipe, title, channel, link,  path):
    path = os.path.expanduser(path)
    pdf = fpdf.FPDF(format='letter') #pdf format
    pdf.add_page() #create new page
    newLineCount = 0
    pdf.set_font("Arial", size=15, style="BU")
    pdf.cell(200, 10, txt=title, align="C", link=link)
    pdf.set_font("Arial", size=12, style="BU")
    pdf.ln()
    pdf.cell(200, 10, txt=channel, align="L")
    pdf.ln()
    pdf.ln()
    pdf.set_font("Arial", size=13, style="BU")

    for line in recipe.splitlines():
        if line.strip() == "":
            newLineCount += 1
            pdf.ln()
        else:
            if newLineCount >= 1:
                pdf.set_font("Arial", size=13, style="BU")
                pdf.multi_cell(200, 10, txt=line, align="L")
                newLineCount = 0
                pdf.set_font("Arial", size=12, style="")
                continue
            pdf.multi_cell(200, 10, txt=line, align="L")
            

    fileName = title.replace(" ", "_")   
    if not os.path.exists(path):
        try:
            os.makedirs(path)
            print(f"Created directory {path}")
        except OSError as e:
            print(f"Error creating directory {path}: {e}")
    try :
        pdf.output(f"{path}/{fileName}.pdf")
        print(f"Saved {fileName}.pdf to {path}")
    except OSError as e:
        print(f"Error saving {fileName}.pdf to {path}: {e}")
       