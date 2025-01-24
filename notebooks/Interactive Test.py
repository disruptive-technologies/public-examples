import marimo

__generated_with = "0.10.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    slider = mo.ui.slider(start=0, stop=15, step=1, value=0)
    slider
    return (slider,)


@app.cell
def _(mo, slider):
    mo.md(f'Value: {slider.value}')
    return


if __name__ == "__main__":
    app.run()
