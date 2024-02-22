# 🌟 Принципы SOLID в Python 🌟

Принципы SOLID — это основополагающие принципы для создания эффективного, масштабируемого и поддерживаемого ПО на Python.

---

## 📐 S - Принцип единственной ответственности (Single Responsibility Principle)

> "Один класс — одна задача."

### Пример в Python:
```python
class Report:
    def generate(self):
        pass

class ReportSaver:
    def save(self, report):
        pass
```
<details>
<summary>🔍 Подробное описание</summary>
В этом примере, класс `Report` отвечает только за генерацию отчета, а `ReportSaver` — за его сохранение. Это демонстрирует принцип единственной ответственности, где каждый класс выполняет только одну функцию.
</details>

---

## 🚪 O - Принцип открытости/закрытости (Open/Closed Principle)

> "Код должен быть открыт для расширения, но закрыт для модификации."

### Пример в Python:
```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        pass
```
<details>
<summary>🔍 Подробное описание</summary>
Здесь `Shape` - это базовый класс, который может быть расширен другими классами, такими как `Circle`. `Circle` расширяет функциональность, не изменяя исходный класс `Shape`, что соответствует принципу открытости/закрытости.
</details>

---

## 🔄 L - Принцип подстановки Барбары Лисков (Liskov Substitution Principle)

> "Объекты должны быть заменяемы на экземпляры их подтипов без нарушения работы программы."

### Пример в Python:
```python
class Bird:
    def fly(self):
        pass

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly")
```
<details>
<summary>🔍 Подробное описание</summary>
В этом примере, класс `Penguin` является подклассом `Bird`, но переопределяет метод `fly` таким образом, что нарушает ожидаемое поведение. Это нарушает принцип Лисков, так как `Penguin` не может быть использован везде, где ожидается `Bird`.
</details>

---

## 🔗 I - Принцип разделения интерфейса (Interface Segregation Principle)

> "Не заставляйте классы зависеть от методов, которые они не используют."

### Пример в Python:
```python
class Worker:
    def work(self):
        pass

class Eater:
    def eat(self):
        pass

class Human(Worker, Eater):
    def work(self):
        pass

    def eat(self):
        pass
```
<details>
<summary>🔍 Подробное описание</summary>
`Human` реализует два интерфейса: `Worker` и `Eater`. Это обеспечивает разделение функциональности, позволяя классу `Human` использовать только необходимые методы, что соответствует принципу разделения интерфейса.
</details>

---

## 🔝 D - Принцип инверсии зависимостей (Dependency Inversion Principle)

> "Компоненты верхнего уровня не должны зависеть от компонентов нижнего уровня."

### Пример в Python:
```python
class Engine:
    def start(self):
        pass



class Car:
    def __init__(self, engine: Engine):
        self.engine = engine
```
<details>
<summary>🔍 Подробное описание</summary>
В этом примере, класс `Car` зависит от абстракции `Engine`, а не от конкретного класса. Это позволяет легко заменять один тип двигателя на другой, не изменяя класс `Car`, что соответствует принципу инверсии зависимостей.
</details>

---

Использование принципов **SOLID** в Python способствует созданию более гибкого, удобного для поддержки и масштабируемого кода.
