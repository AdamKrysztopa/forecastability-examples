# forecastability-examples

Tutorials, walkthroughs, and integrations for the [`dependence-forecastability`](https://github.com/AdamKrysztopa/dependence-forecastability) toolkit

[![Notebooks](https://github.com/AdamKrysztopa/forecastability-examples/actions/workflows/notebooks.yml/badge.svg)](https://github.com/AdamKrysztopa/forecastability-examples/actions/workflows/notebooks.yml)
![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)

---

## Installation

Install the core toolkit with any optional framework extras you need:

```bash
pip install "dependence-forecastability[darts,mlforecast]"
```

Or with `uv`:

```bash
uv add dependence-forecastability
```

For the full examples environment (all extras + dev tooling):

```bash
uv sync --all-extras
```

---

## Quick links

| Directory | Contents |
| --- | --- |
| [`walkthroughs/`](walkthroughs/) | Step-by-step forecastability walkthroughs |
| [`triage_walkthroughs/`](triage_walkthroughs/) | Focused single-capability triage notebooks |
| [`recipes/`](recipes/) | Short framework-integration snippets |

---

## Notebook index

| Notebook | Description | Dataset |
| --- | --- | --- |
| *(notebooks arriving via EX-MIG-01)* | — | — |

---

## Where to file issues

| Issue type | Where |
| --- | --- |
| Bugs in triage logic or the public API | [dependence-forecastability issues](https://github.com/AdamKrysztopa/dependence-forecastability/issues) |
| Bugs in notebooks or framework wiring | [forecastability-examples issues](https://github.com/AdamKrysztopa/forecastability-examples/issues) |

---

## Development

```bash
git clone https://github.com/AdamKrysztopa/forecastability-examples.git
cd forecastability-examples
uv sync --all-extras
uv run jupyter lab
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

MIT — see [LICENSE](LICENSE).
