import markdown
import os
import csv

path = os.path.dirname(os.path.dirname(__file__))
output_path = os.path.dirname(__file__) + "/result/"
name_file_member_association = []
event_association = []

def loadFiles():
    dir_list = os.listdir(path)
    for file in dir_list:
        if file.endswith(".csv"):
            loadCSV(os.path.join(path, file))
        if file.endswith(".md"):
            loadMD(file)

def loadMD(file):
    full_file_path = os.path.join(path, file)
    with open(full_file_path, "r", encoding="utf-8") as f:
        content = f.read()
        html_body = markdown.markdown(content)
        event_association.append(file.replace(".md", ".html"))

        splited = file.replace(".md", "").split('-')[-1]
        dir_list = os.listdir(path)
        image = None
        for ff in dir_list:
            if ff.endswith("webp"):
                ffp = os.path.join(path, ff)
                nameImage = ffp.replace(".webp", "").split("-")[-1]
                if (nameImage == splited):
                    image = ffp
        html_body = html_body + f"""<img src="{image}" alt="">"""
        html_complete = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <link rel="stylesheet" href="style.css">
                <title>{file.replace(".md", "")}</title>
            </head>
            <body>
                {html_body}
            </body>
            </html>
            """
        html_file_path = os.path.join(output_path, file.replace(".md", ".html"))
        with open(html_file_path, "w", encoding="utf-8") as b:
            b.write(html_complete)

def loadCSV(file):
    with open(file, 'r') as csvfile:
        html_body = ""
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            name = row[0]
            lastname = row[1]
            email = row[2]
            fonction = row[3]
            html_body = html_body + f"<div>Prénom : {name}\nNom : {lastname}\nEmail : {email}\nFonction : {fonction}</div>"

        nameFile = os.path.basename(file).split('/')[-1].replace(".csv", ".html")
        name_file_member_association.append(output_path + nameFile)
        with open(output_path + nameFile, "w", encoding="utf-8") as f:
            html_complete = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <link rel="stylesheet" href="style.css">
                        <title>{file.replace(".md", "")}</title>
                    </head>
                    <body>
                        {html_body}
                    </body>
                    </html>
                    """
            f.write(html_complete)

def loadIndex():
    s = ""
    for e in event_association:
        s = s + f"""<div><a href="{e}">{e}</a></div>"""
    with open(output_path + "index.html", "w", encoding="utf-8") as f:
        html_complete = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <link rel="stylesheet" href="style.css">
                    <title>Home Page</title>
                </head>
                <body>
                    <h1>Actualités de l'association</h1>
                    <div><a href="/{name_file_member_association[0]}">membre du bureau de l'association</a></div>
                    {s}
                </body>
                </html>
                """
        f.write(html_complete)


if __name__ == "__main__":
    loadFiles()
    print("Chargement des fichier effectués !")
    loadIndex()
