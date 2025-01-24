import marimo

__generated_with = "0.10.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import disruptive as dt
    return dt, mo


@app.cell
def _(mo):
    inp_project_id = mo.ui.text(label='Project ID')
    inp_project_id
    return (inp_project_id,)


@app.cell
def _(dt, inp_project_id, mo):
    def print_devices():
        if len(inp_project_id.value) == 0:
            return mo.md('Input a valid Project ID.')

        msg = ''
        try:
            for device in dt.Device.list_devices(inp_project_id.value):
                msg += f'{device.device_id}  \n'
        except Exception as e:
            msg = str(e)
            
        return mo.md(msg)


    print_devices()
    return (print_devices,)


if __name__ == "__main__":
    app.run()
