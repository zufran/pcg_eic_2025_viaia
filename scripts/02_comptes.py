import fitz  # PyMuPDF
import os
import datetime

def pdf_vers_texte(chemin_pdf, dossier_sortie, nom_script):
    with fitz.open(chemin_pdf) as doc:
        texte = "".join(page.get_text() for page in doc)
        debut = texte.find("Les comptes imprimés en caractères italiques sont d’utilisation facultative.")
        fin = texte.find("Chapitre III – Règles d’établissement d’un plan de comptes")

        if debut != -1 and fin != -1 and fin > debut:
            texte = texte[debut + len("Les comptes imprimés en caractères italiques sont d’utilisation facultative."):fin].strip()
            # Enlever les lignes vides
            lignes = [ligne for ligne in texte.splitlines() if ligne.strip()]

            # Liste pour stocker les lignes à ignorer
            lignes_a_ignorer = set()

            # Supprimer les lignes qui commencent par "CLASSE" et celles contenant "RECUEIL DES NORMES COMPTABLES FRANÇAISES"
            # et les lignes contenant "Version du 1er janvier 2025" et la suivante
            for i, ligne in enumerate(lignes):
                if "Version du 1er janvier 2025" in ligne:
                    lignes_a_ignorer.add(i)  # Ajoute cette ligne
                    if i + 1 < len(lignes):
                        lignes_a_ignorer.add(i + 1)  # Ajoute la ligne suivante

            # Filtrer les lignes à ignorer
            lignes = [ligne for i, ligne in enumerate(lignes) if i not in lignes_a_ignorer]
            
            # Supprimer les lignes qui commencent par "CLASSE" et celles contenant "RECUEIL DES NORMES COMPTABLES FRANÇAISES"
            lignes = [ligne for ligne in lignes if not ligne.startswith("CLASSE") and "RECUEIL DES NORMES COMPTABLES FRANÇAISES" not in ligne]

            texte = "\n".join(lignes)
        else:
            texte = "Section introuvable"

    nom_sortie = f"{nom_script}_{datetime.datetime.now().strftime('%H_%M_%S-%d_%m_%Y')}-{os.path.basename(chemin_pdf)[:-4]}.txt"
    os.makedirs(dossier_sortie, exist_ok=True)

    with open(os.path.join(dossier_sortie, nom_sortie), 'w', encoding='utf-8') as f:
        f.write(texte)
    print(f"Export réussi : {os.path.join(dossier_sortie, nom_sortie)}")

if __name__ == "__main__":
    dossier_parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pdf_trouve = next((f for f in os.listdir(dossier_parent) if f.endswith('.pdf')), None)

    if pdf_trouve:
        pdf_vers_texte(os.path.join(dossier_parent, pdf_trouve),
                       os.path.join(dossier_parent, "data"),
                       os.path.splitext(os.path.basename(__file__))[0])
    else:
        print("Aucun PDF trouvé dans le dossier parent")
