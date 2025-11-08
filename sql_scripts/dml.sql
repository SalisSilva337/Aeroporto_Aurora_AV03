-- Inserindo passageiros
INSERT INTO Passageiro (Nome, Email, Telefone)
VALUES
('João Silva', 'joao@email.com', '119999999'),
('Maria Souza', 'maria@email.com', '219888888'),
('Carlos Lima', 'carlos@email.com', '319777777');

-- Inserindo voos
INSERT INTO Voo (Local_Partida, Local_Destino, Distancia, Disponibilidade)
VALUES
('São Paulo', 'Rio de Janeiro', 400.5, TRUE),
('Brasília', 'Lisboa', 7500.0, TRUE);

-- Inserindo reservas
INSERT INTO Reserva (ID_passageiro, ID_voo, Numeracao, Classe, MetodoPagamento, QuantidadePassageiros, Data)
VALUES
(1, 1, 'RES123', 'Economica', 'Cartão de Crédito', 1, '2025-09-01'),
(2, 2, 'RES124', 'Executiva', 'PIX', 2, '2025-09-02');

-- Inserindo tripulações
INSERT INTO Tripulacao (ID_voo, Pilotos, Navegador, MecanicoRadio, ComissariosBordo, MecanicosVoo)
VALUES
(1, 2, 1, 1, 3, 1),
(2, 3, 1, 2, 5, 2);


-- Inserindo avioes
INSERT INTO Aviao (Modelo, Capacidade) 
VALUES
('Boeing 737-800', 189),
('Airbus A320neo', 180),
('Embraer E195-E2', 132),
('Boeing 777-300ER', 396),
('Airbus A350-900', 350);
