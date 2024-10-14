public class Main {
    public static void main(String[] args) {
        // Создание двух матриц комплексных чисел размером 3x3
        ComplexNumber[][] mat1Data = {
                {new ComplexNumber(4, 2), new ComplexNumber(6, 8), new ComplexNumber(10, 12)},
                {new ComplexNumber(12, 16), new ComplexNumber(18, 20), new ComplexNumber(22, 24)},
                {new ComplexNumber(26, 28), new ComplexNumber(30, 32), new ComplexNumber(36, 40)}
        };
        Matrix matrix1 = new Matrix(mat1Data);

        System.out.println("первая матрица:");
        System.out.println(matrix1);


        ComplexNumber[][] mat2Data = {
                {new ComplexNumber(2, 1), new ComplexNumber(3, 4), new ComplexNumber(5, 6)},
                {new ComplexNumber(6, 8), new ComplexNumber(9, 10), new ComplexNumber(11, 12)},
                {new ComplexNumber(13, 14), new ComplexNumber(15, 16), new ComplexNumber(18, 20)}
        };
        Matrix matrix2 = new Matrix(mat1Data);

        System.out.println("вторая матрица:");
        System.out.println(matrix2);

        // Операция сложения
        Matrix sumMatrix = matrix1.add(matrix2);
        System.out.println("Сложение матриц:");
        System.out.println(sumMatrix);

        // Операция вычитания
        Matrix differenceMatrix = matrix1.subtract(matrix2);
        System.out.println("Вычитание:");
        System.out.println(differenceMatrix);

        // Операция умножения
        try {
            Matrix productMatrix = matrix1.multiply(matrix2);
            System.out.println("Умножение:");
            System.out.println(productMatrix);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }


        // Операция транспонирования
        Matrix transposeMatrix = matrix1.transpose();
        System.out.println("Транспонирование 1:");
        System.out.println(transposeMatrix);


        Matrix inverseMatrix = matrix2.getInverse();
        System.out.println("обратная 2:");
        System.out.println(inverseMatrix);


        // Вычисление детерминанта первой матрицы
        try {
            ComplexNumber determinant = matrix1.getDeterminant();
            System.out.println("Детерминант 1: " + determinant);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }

        // Операция деления (умножение на обратную матрицу)
        try {
            Matrix divisionMatrix = matrix1.divide(matrix2);
            System.out.println("\nДеление матриц (1 / 2):");
            System.out.println(divisionMatrix);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }





        int matrixSize = 3; // Размер матрицы
        int mod = 10; // Ограничение для генерации случайных чисел

        // Инициализация матрицы с нулями
        Matrix randomMatrix = new Matrix(matrixSize, matrixSize);

        randomMatrix.randomDoubleFill(mod);
        System.out.println("Случайная матрица с дробными числами:");
        System.out.println(randomMatrix);

        // Заполнение матрицы случайными целыми числами
        randomMatrix.randomIntFill(mod);
        System.out.println("Случайная матрица с целыми числами:");
        System.out.println(randomMatrix);

        // Тестирование методов getter и setter
        System.out.println("getter и setter:");

        // Используем getter для вывода определенного элемента (например, 1,1)
        ComplexNumber element = randomMatrix.getElement(1, 1);
        System.out.println("Элемент в позиции (1, 1): " + element);

        // Устанавливаем новое значение для элемента (1,1) с помощью setter
        randomMatrix.setElement(new ComplexNumber(100, 200), 1, 1);
        System.out.println("Матрица после изменения элемента в позиции (1, 1):");
        System.out.println(randomMatrix);

        // Проверяем новое значение, используя getter
        ComplexNumber newElement = randomMatrix.getElement(1, 1);
        System.out.println("Новое значение элемента в позиции (1, 1): " + newElement);

    }
}