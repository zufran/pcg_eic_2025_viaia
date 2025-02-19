import fitz, os, datetime

def pdf_vers_texte(chemin_pdf, dossier_sortie, nom_script):
    nom_fichier = os.path.basename(chemin_pdf).replace('.pdf', '')
    horodatage = datetime.datetime.now().strftime("%H_%M_%S-%d_%m_%Y")
    chemin_txt = os.path.join(dossier_sortie, f"{nom_script}_{horodatage}-{nom_fichier}.txt")
    os.makedirs(dossier_sortie, exist_ok=True)
    with fitz.open(chemin_pdf) as document, open(chemin_txt, 'w', encoding='utf-8') as f:
        f.write("".join(page.get_text() for page in document))
    print(f"Texte extrait dans : {chemin_txt}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dossier_parent = os.path.dirname(script_dir)
    pdf_trouves = [f for f in os.listdir(dossier_parent) if f.endswith('.pdf')]
    
    if pdf_trouves:
        pdf_vers_texte(
            os.path.join(dossier_parent, pdf_trouves[0]),
            os.path.join(dossier_parent, "data"),
            os.path.splitext(os.path.basename(__file__))[0]
        )
    else:
        print("Aucun PDF trouvé dans le dossier parent")