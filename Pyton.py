import sqlite3
conn = sqlite3.connect("avengers.db")
cursor = conn.cursor()
print("Conexion establecida correctamente.")


def mostrar_superheroes():
    cursor.execute("SELECT * FROM avengers")
    superheroes = cursor.fetchall()

    if superheroes:
        for heroe in superheroes:
            print(heroe)
    else:
        print("No hay avengers registrados.")


while True:
    print("\n===== MENU DE SUPERHEROES =====")
    print("1. Mostrar todos los avengers")
    print("2. Buscar por id")
    print("3. Agregar un vengador")
    print("4. Modificar la habilidad de un superheroe")
    print("5. Eliminar un vengador")
    print("6. Salir")

    opcion = input("Elegi una opcion: ")

    # 1. Mostrar todos los superheroes
    if opcion == "1":
        mostrar_superheroes()

    # 2. Buscar por id
    elif opcion == "2":
        id = input("Ingresa el id que queres buscar: ")

        cursor.execute(
            "SELECT * FROM avengers WHERE id = ?",
            (id,)
        )

        superheroes = cursor.fetchall()

        if superheroes:
            for heroe in superheroes:
                print(heroe)
        else:
            print("No se encontraron superheroes con esa habilidad.")

    # 3. Agregar un superheroe
    elif opcion == "3":
        nombre = input("Ingresa el nombre del superheroe: ")
        habilidad = input("Ingresa su habilidad: ")

        cursor.execute(
            "INSERT INTO avengers (nombre, habilidad) VALUES (?, ?)",
            (nombre, habilidad)
        )

        conn.commit()

        print("Superheroe agregado correctamente.")
        print("Tabla actualizada:")
        mostrar_superheroes()

    # 4. Modificar la habilidad
    elif opcion == "4":
        nombre = input("Ingresa el nombre del superheroe que queres modificar: ")
        habilidad = input("Ingresa la nueva habilidad: ")

        cursor.execute(
            "UPDATE avengers SET habilidad = ? WHERE nombre = ?",
            (habilidad, nombre)
        )

        conn.commit()

        print("Superheroe actualizado correctamente.")
        print("Tabla actualizada:")
        mostrar_superheroes()

    # 5. Eliminar un superheroe
    elif opcion == "5":
        nombre = input("Ingresa el nombre del superheroe que queres eliminar: ")

        cursor.execute(
            "DELETE FROM avengers WHERE nombre = ?",
            (nombre,)
        )

        conn.commit()
        print("Superheroe eliminado correctamente.")

        print("Tabla actualizada:")
        mostrar_superheroes()

    # 6. Salir
    elif opcion == "6":
        print("Cerrando el programa...")
        break

    else:
        print("Opcion invalida. Elegi un numero del 1 al 6.")

conn.close()
print("Conexion cerrada.")