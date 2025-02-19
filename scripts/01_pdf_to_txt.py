import fitz  # PyMuPDF
import os
import datetime

def pdf_to_text(pdf_path, output_dir, script_name):
    # Ouvrir le fichier PDF et extraire le texte
    pdf_document = fitz.open(pdf_path)
    text = "".join(page.get_text() for page in pdf_document)

    # Obtenir la date et l'heure actuelles
    timestamp = datetime.datetime.now().strftime("%H_%M_%S-%d_%m_%Y")

    # Nom du fichier PDF sans l'extension
    pdf_filename = os.path.splitext(os.path.basename(pdf_path))[0]

    # Nom du fichier TXT avec horodatage et préfixe du nom du script
    txt_filename = f"{script_name}_{timestamp}-{pdf_filename}.txt"
    txt_path = os.path.join(output_dir, txt_filename)

    # Écrire le texte extrait dans un fichier TXT
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)

    print(f"Le texte a été extrait et sauvegardé dans {txt_path}")

if __name__ == "__main__":
    # Chemins des répertoires
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    output_dir = os.path.join(parent_dir, "data")

    # Nom du script sans extension
    script_name = os.path.splitext(os.path.basename(__file__))[0]

    # Rechercher le fichier PDF dans le dossier parent
    pdf_files = [f for f in os.listdir(parent_dir) if f.endswith('.pdf')]
    if not pdf_files:
        print("Aucun fichier PDF trouvé dans le dossier parent.")
    else:
        pdf_path = os.path.join(parent_dir, pdf_files[0])

        # Créer le dossier de sortie s'il n'existe pas
        os.makedirs(output_dir, exist_ok=True)

        # Appeler la fonction pour convertir le PDF en TXT
        pdf_to_text(pdf_path, output_dir, script_name)
