from back.addtotable import insert_csv_row

def load_csv(path, cursor, ville):
    """ This function load and read the csv file, and insert row in db file.

    cursor : It acts like a position indicator and will be mostly use to
    retrieve data.

    path : Source of the csv file.

    """
    with open(path, "r", encoding="utf-8") as f:    
        f.readline()
        line = f.readline()
        while line:
            insert_csv_row(line, cursor, ville)
            line = f.readline()
    # logging.info('load_csv: Charge la base de données')
