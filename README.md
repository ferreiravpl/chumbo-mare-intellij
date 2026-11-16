# Chumbo + Maré — IntelliJ

Tema para IDEs JetBrains **2025.3 ou mais novos** no Linux: interface **Islands Dark** com o
esquema de cores **Chumbo + Maré** no editor. Precisa só de `python3`.

## Instalar

```bash
git clone https://github.com/ferreiravpl/chumbo-mare-intellij.git ~/chumbo-mare-intellij
cd ~/chumbo-mare-intellij
./install.sh                              # com o IDE aberto: detecta instalação e perfil
./install.sh ~/.local/opt/intellij-idea   # ou aponte a instalação (o IDE pode estar fechado)
```

Reinicie o IDE e escolha **Settings › Appearance › Theme → Chumbo + Maré**. O esquema de cores
do editor vem junto.

## Desinstalar

```bash
./uninstall.sh                            # mesmos argumentos do install.sh
```

Reinicie o IDE e ele volta ao tema padrão.

## Paleta

| Papel | Cor |
|---|---|
| Fundo do editor / linha atual | `#191A1C` · `#1F2023` |
| Guias de indentação | `#26282C` |
| Destaque | `#E9F0C9` · `#CAD89E` |
| Texto | `#E0E0E0` |

| Elemento de código | Cor | Itálico |
|---|---|---|
| Keyword | `#E9F0C9` | — |
| Método (declaração e chamada) | `#F4F8E4` | sim |
| Tipo | `#F4F8E4` | — |
| Anotação | `#CAD89E` | — |
| String | `#A9B39A` | — |
| Número | `#C3D97C` | — |
| Comentário | `#66808B` | sim |

## Como é gerado

O `build.py` lê o Islands Dark do próprio IDE (nada da JetBrains é redistribuído aqui), troca o
nome, aponta o esquema `scheme/ChumboMare.icls` e empacota tudo num plugin `.jar` em
`~/.local/share/JetBrains/<perfil>/chumbo-mare-theme/`.

Para ajustar uma cor, edite `scheme/ChumboMare.icls` (ou ajuste no IDE e exporte o esquema por
cima desse arquivo) e rode o `install.sh` de novo.

## Licença

[GPL-3.0](LICENSE).
