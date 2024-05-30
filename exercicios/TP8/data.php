<?php
$dsn = 'sqlite:sensors.db'; # Aceder a db

/*
UALG - 2023/2024
Disciplina - POO
a64108 - André Vieira
*/

try {
    $pdo = new PDO($dsn);   # Nova instancia PDO para ligar a db com o DNS
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); # Dá flag de exceções sempre que há um erro nas operações da db

    $stmt = $pdo->query('SELECT idReading, idSensor, timestamp, value FROM Reading'); # Vai a db e seleciona todas as linhas da tabela e retorna em formato PDOstatement
    $readings = $stmt->fetchAll(PDO::FETCH_ASSOC); # Pega nas linhas copiadas como um array e depois separa por colunas

    if ($readings) {
        foreach ($readings as $row) {
            echo "<tr>
                    <td>{$row['idReading']}</td>
                    <td>{$row['idSensor']}</td>
                    <td>{$row['timestamp']}</td>
                    <td>{$row['value']}</td>
                  </tr>";
        }
    } else {
        echo "<tr><td colspan='4'>Sem dados disponiveis</td></tr>";
    }
} catch (PDOException $e) {
    echo "Error: " . $e->getMessage(); # Captura exceções e envia uma mensagem de erro com a exceçao encontrada
}

?>
