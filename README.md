# Extracting data from the [Spanish Statistical Office (INE)](https://www.ine.es/en/index.htm)

The Spanish Statistical Office provides an API to extract data.
- The request is of the form `https://servicios.ine.es/wstempus/jsstat/{language}/DATASET/{table_id}`
    - The language can be `EN` (English) or `ES` (Spanish)
    - The table ID is obtained by looking at the `t` parameter of the table we want to extract
        - For example, the ID of the table ["Immigration flow from abroad by year, sex and age"](https://www.ine.es/jaxiT3/Tabla.htm?t=24387&L=1) is `24387`
- The data is returned as a [JSON-stat](https://json-stat.org) object. We can use the library `pyjstat` to easily process this object and convert it to a pandas dataframe
- More instructions [here](https://www.ine.es/dyngs/DataLab/en/manual.html?cid=1259945948447) (although no English version!)

The `main.py` file can be run as a notebook thanks to `jupytext`. Just open it from a Jupyter environment. Remember that you will need to save it as a regular jupyter notebook if you would like to keep the results. Refer to the [official repo](https://github.com/mwouts/jupytext) for more information.
