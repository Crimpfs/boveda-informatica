#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <windows.h>

using namespace std;

FILE* fd;

void escribir() {
    char buffer[50];
    cin.ignore(); // Clear leftover newline
    cout << "Mensaje:" << endl;
    cin.getline(buffer, 50);

    errno_t err = fopen_s(&fd, "personas.txt", "w"); // safer fopen
    if (err == 0 && fd != nullptr) {
        fputs(buffer, fd);
        fclose(fd);
    }
    else {
        cout << "No se pudo crear el archivo" << endl;
    }
}

void agregar() {
    char buffer[50];
    cin.ignore(); // Clear leftover newline
    cout << "Mensaje:" << endl;
    cin.getline(buffer, 50);

    errno_t err = fopen_s(&fd, "personas.txt", "a"); // safer fopen
    if (err == 0 && fd != nullptr) {
        fputs(buffer, fd);
        fclose(fd);
    }
    else {
        cout << "No se pudo agregar en el archivo" << endl;
    }
}

void leer() {
    errno_t err = fopen_s(&fd, "personas.txt", "r");
    if (err == 0 && fd != nullptr) {
        char k;
        while ((k = fgetc(fd)) != EOF) {
            cout << k;
            Sleep(500);
        }
        fclose(fd);
        cout << endl;
    }
    else {
        cout << "No se pudo abrir el archivo" << endl;
    }
}

void eliminar() {
    if (remove("personas.txt") == 0)
        cout << "Archivo eliminado correctamente" << endl;
    else
        cout << "No se pudo eliminar el archivo" << endl;
}

void renombrar() {
    if (rename("personas.txt", "people.txt") == 0)
        cout << "Archivo renombrado correctamente" << endl;
    else
        cout << "No se pudo renombrar el archivo" << endl;
}

int main() {
    int opt;
    do {
        cout << "1. Escribir\n2. Leer\n3. Eliminar\n4. Renombrar\n5. Agregar\n6. Salir" << endl;
        cout << "Seleccione una opción: ";
        cin >> opt;

        switch (opt) {
        case 1: escribir(); break;
        case 2: leer(); break;
        case 3: eliminar(); break;
        case 4: renombrar(); break;
        case 5: agregar(); break;
        case 6: break;
        default: cout << "Opción inválida" << endl;
        }
    } while (opt != 6);

    return 0;
}
