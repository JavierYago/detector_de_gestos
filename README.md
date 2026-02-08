# detector de gestos

Proyecto para detectar gestos (Detector de gestos).

Descripción
- Código principal en `main.py` y lógica de diagnóstico en `diagnostico.py`.

Uso rápido
1. Crear entorno virtual e instalar dependencias (si aplica):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Ejecutar la aplicación:

```powershell
.\.venv\Scripts\python.exe main.py
```

Subir a GitHub (opciones)
- Opción A (con GitHub CLI `gh`):

```bash
gh repo create detector-de-gestos --public --source=. --remote=origin --push
```

- Opción B (manual):

```bash
git remote add origin https://github.com/<usuario>/detector-de-gestos.git
git branch -M main
git push -u origin main
```

Notas
- Reemplaza `<usuario>` por tu usuario de GitHub.
- Si quieres que yo cree el repositorio remoto, indícame si tienes `gh` configurado o dame permiso para usar la CLI aquí.
