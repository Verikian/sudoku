# Voice controlled Sudoku 

This student project is a common effort of:
- **Katarzyna Kleczkowska** ()
- **Adam Sitko** (Verikian)

### EN Instruction - how to use:

- Install the requirements (instruction below)
- Run main.py file `python main.py`
- In order to record a voice command, press the *'Start'* button, which is located below the Sudoku. The user has 7 seconds to say the command (only Polish command are supported).
- In order to select the box (field) into which the user wants to enter the number, use the coordinates visible on the board (eg *'Barbara trzy'*).
- After entering the coordinates, pronounce the number to be entered (e.g. *'Barbara trzy, wpisz sześć'* = Barbara three, enter six).
- If, after entering the coordinates, the number 0 is pronounced or the word *'usuń'* (delete) is entered, the value in the cell will be removed (e.g. *'Barbara trzy, wpisz zero'* ('Barbara three, enter zero'), *'Barbara trzy, usuń wartość'* (Barbara three, delete the value).

Examples:
- We want to enter the number 5 in row 4 in column 7. We can achieve this with the following commands: *'Dorota siedem, wpisz pięć'*, *'Dorota siedem, pięć'* (Dorothy seven, enter five, Dorothy seven, five)
- We want to remove the number 5 from row 4 from column 7. We will achieve this with the following commands: *'Dorothy seven, delete the value'*, *'Dorothy seven, enter zero'*, *'Dorothy seven, delete'* (Dorota siedem, usuń wartość, Dorota siedem, wpisz zero, Dorota siedem, usuń)

### PL Instrukcja użycia:
- Zainstaluj wymagane biblioteki (instrukcja poniżej)
- Uruchom plik main.py `python main.py`
- W celu nagrania komendy głosowej należy nacisnąć przycisk *'Start'*, który znajduje się poniżej sudoku. Użytkownik ma 7 sekund na wypowiedzenie komendy (tylko polskie komendy)
- Aby wybrać kratkę, do której ma zostać wpisana liczba, należy posłużyć się współrzędnymi widocznymi na planszy (np. *'Barbara trzy'*).
- Po podaniu współrzędnych, należy podać liczbę, która ma zostać wpisana (np. *'Barbara trzy, wpisz sześć'*.
- Jeżeli po podaniu współrzędnych zostanie podana liczba 0, bądź padnie słowo *'usuń'*, wartość znajdująca się w komórce zostanie usunięta (np. *'Barbara trzy, wpisz zero'*, *'Barbara trzy, usuń wartość'*).

Przykłady:
- Chcemy wpisać liczbę 5 w wierszu 4 w kolumnie 7. Możemy to osiągnąć komendami: *'Dorota siedem, wpisz pięć'*, *'Dorota siedem, pięć'*
- Chcemy usunąć liczbę 5 z wiersza 4 z kolumny 7. Osiągniemy to komendami: *'Dorota siedem, usuń wartość'*, *'Dorota siedem, wpisz zero'*, *'Dorota siedem, usuń'*


# Requirements management
Python version: at least 3.10

The convention for managing Python dependencies is as follows:

- install pip-tools: `python -m pip install pip-tools` more: [https://pypi.org/project/pip-tools/](https://pypi.org/project/pip-tools/)
- required libraries are already added into requirements.in
- call `pip-compile` to create requirements.txt

# Troubleshooting
If a problem with SSL Certificate appears, try this command in your terminal

```
sudo /Applications/Python\ 3.10/Install\ Certificates.command ; exit; -- pip install --upgrade certifi
```