"""Rakit prototipe: sisipkan lambang ke halaman dan hasilkan index.html mandiri."""
import pathlib, sys
here = pathlib.Path(__file__).parent
page = (here / "src/page.html").read_text(encoding="utf-8")
emblem = (here / "src/emblem-inner.svg").read_text(encoding="utf-8")
page = page.replace("<!--EMBLEM-->", emblem)
(here / "index.html").write_text(
    '<!doctype html>\n<html lang="id">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    + page.replace("</style>", "</style>\n</head>\n<body>", 1) + "\n</body>\n</html>\n",
    encoding="utf-8")
if len(sys.argv) > 1:  # salinan tanpa kerangka dokumen (untuk pratinjau artifact)
    pathlib.Path(sys.argv[1]).write_text(page, encoding="utf-8")
print("ok")
