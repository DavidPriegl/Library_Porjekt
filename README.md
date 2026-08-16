# Könyvtári nyilvántartó rendszer

## Bevezetés

A projekt célja a Python objektumorientált programozás (OOP) gyakorlati alkalmazásának bemutatása. A rendszer egy egyszerű könyvtári nyilvántartási modell, amely lehetővé teszi könyvek és DVD-k katalogizálását, tagok regisztrálását, valamint a kölcsönzés és visszavétel kezelését.

A feladat nem csupán a program logikai működésének megvalósítását szolgálja, hanem az OOP alapelvek, így az osztályok, az öröklés, a kapszulázás és az adatelemzés alkalmazásának gyakorlását is.

## Célkitűzés

A projektben a következő célokat valósítjuk meg:

- különböző dokumentumtípusok modellezése osztályok segítségével;
- az öröklési kapcsolat kialakítása a közös tulajdonságok és metódusok között;
- adatintegritás biztosítása validációs ellenőrzésekkel;
- tagok és könyvtári elemek kezelésének megoldása;
- kölcsönzési műveletek logikai ellenőrzése és hibakezelése.

## Főbb komponensek

### Item
A közös alaposztály, amely a könyvtári elemek közös attribútumait és működését definiálja. Ide tartoznak az azonosító, a cím és a kölcsönzési állapot.

### Book
A könyvek saját osztálya, amely kibővíti az alaposztályt a szerző és a műfaj attribútumokkal.

### DVD
A DVD-k saját osztálya, amely a hossz paraméterét kezeli, és a megfelelő validációs feltételek mellett történő létrehozást biztosítja.

### Member
A könyvtári tagok osztálya, amely a név, az azonosító és a kölcsönzött tételek nyilvántartását kezeli.

### Library
A könyvtár fő entitása, amely összefogja a katalógus és a tagok adatainak kezelését, valamint a kölcsönzés és visszavétel műveleteit.

## Funkcionalitás

A rendszer képes a következő műveletek végrehajtására:

- új könyvek és DVD-k hozzáadása a katalógushoz;
- új tagok regisztrálása;
- egy adott elem kölcsönzése és visszavétele;
- már kölcsönzött elem újbóli kölcsönzési kísérletének tiltása;
- műfaj szerinti keresés könyvek között;
- hibaesetek kezelése érdemi üzenetekkel.

## Összegzés

A könyvtári nyilvántartó rendszer példamutató megoldás arra, hogy a Python nyelvben hogyan lehet valós világbeli fogalmakat modellezni osztályok és objektumok segítségével. A projekt alkalmas a gyakorlati OOP ismeretek elmélyítésére és a strukturált, jól dokumentált kódírás elsajátítására.
