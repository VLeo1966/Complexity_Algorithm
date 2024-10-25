# Complexity_Algorithm

Чтобы оценить сложность одного из ранее созданных алгоритмов, выберем, к примеру, алгоритм **пузырьковой сортировки** из предыдущих примеров.

### Оценка сложности пузырьковой сортировки:
- **Временная сложность**:
  - В худшем случае, для отсортированного в обратном порядке массива, каждый элемент нужно будет сравнить со всеми остальными, что приводит к двойному вложенному циклу. 
  - Для массива из `n` элементов пузырьковая сортировка выполняет примерно \((n-1) + (n-2) + ... + 1 = \frac{n \cdot (n-1)}{2} \approx O(n^2)\) операций.
  - Поэтому **временная сложность пузырьковой сортировки** составляет \(O(n^2)\) в худшем и среднем случаях.
  - В лучшем случае (если массив уже отсортирован), пузырьковая сортировка может работать за \(O(n)\), если реализация включает флаг завершения.

- **Пространственная сложность**:
  - Алгоритм работает **на месте** (in-place), используя только несколько дополнительных переменных для счётчиков и обмена значений.
  - **Пространственная сложность** составляет \(O(1)\).
