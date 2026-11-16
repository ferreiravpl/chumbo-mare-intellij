"""Chumbo + Maré para IntelliJ — gera o plugin de tema a partir do IDE instalado.

Interface: o Islands Dark do próprio IDE, sem alteração de cor (só muda o nome e
aponta o esquema do editor). Nada da JetBrains é redistribuído: o tema é lido do
IDE na hora da instalação.
Editor: o esquema "Chumbo + Maré" deste repositório (scheme/ChumboMare.icls).

Uso: python3 build.py <diretório-do-IDE> <saída.jar>
"""
import json
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
IDE = Path(sys.argv[1])
OUT = Path(sys.argv[2])
VERSION = "1.0.0"

THEME_SRC = "themes/islands/ManyIslandsDark.theme.json"
SCHEME = HERE / "scheme" / "ChumboMare.icls"

PLUGIN_XML = f"""<idea-plugin>
  <id>local.chumbo-mare-theme</id>
  <name>Chumbo + Maré Theme</name>
  <version>{VERSION}</version>
  <vendor>ferreiravpl</vendor>
  <description>Interface Islands Dark com o esquema de cores Chumbo + Maré no editor.</description>
  <idea-version since-build="253"/>
  <depends>com.intellij.modules.platform</depends>
  <extensions defaultExtensionNs="com.intellij">
    <themeProvider id="chumbo-mare" path="/themes/ChumboMare.theme.json" targetUi="islands"/>
  </extensions>
</idea-plugin>
"""


def read_from_ide(entry):
    """O jar que guarda o Islands muda entre versões (app.jar no 2025.3,
    intellij.platform.resources.jar no 2026.x): procura em todos do lib/."""
    for path in sorted((IDE / "lib").glob("*.jar")):
        with zipfile.ZipFile(path) as jar:
            if entry in jar.namelist():
                return jar.read(entry).decode("utf-8")
    sys.exit(f"{entry} não encontrado em {IDE}/lib — o IDE precisa ser 2025.3 ou mais novo")


def main():
    theme = json.loads(read_from_ide(THEME_SRC))
    theme["name"] = "Chumbo + Maré"
    theme["author"] = "ferreiravpl"
    theme["editorScheme"] = "/themes/ChumboMare.xml"

    OUT.parent.mkdir(parents=True, exist_ok=True)
    tmp = OUT.with_suffix(".tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("META-INF/plugin.xml", PLUGIN_XML)
        z.writestr("themes/ChumboMare.theme.json", json.dumps(theme, indent=2, ensure_ascii=False))
        z.writestr("themes/ChumboMare.xml", SCHEME.read_text(encoding="utf-8"))
    # troca atômica: o IDE aberto pode estar com o jar antigo mapeado
    tmp.replace(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
