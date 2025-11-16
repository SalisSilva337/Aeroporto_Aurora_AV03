INSERT INTO Passageiro (Nome, Email, Telefone, Senha)
VALUES
('João Silva', 'joao@email.com', '119999999', '\\x1234abcd'),
('Maria Souza', 'maria@email.com', '219888888', '\\xa1b2c3d4'),
('Carlos Lima', 'carlos@email.com', '319777777', '\\x99aa88cc');

INSERT INTO Aviao (Modelo, Capacidade) VALUES
('Boeing 737-800', 189),
('Airbus A320neo', 180),
('Embraer E195-E2', 132),
('Boeing 777-300ER', 396),
('Airbus A350-900', 350);


INSERT INTO Voo (Local_Partida, Local_Destino, Disponibilidade, Duracao, ID_Aviao) VALUES
('São Paulo', 'Rio de Janeiro', TRUE, '01:10',1),
('Brasília', 'Salvador', TRUE, '02:15',2),
('Curitiba', 'Belo Horizonte', TRUE, '01:45',3),
('Recife', 'Fortaleza', TRUE, '01:00',4),
('Porto Alegre', 'Florianópolis', TRUE, '00:50',5);


INSERT INTO Reserva (ID_passageiro, ID_voo, Classe, MetodoPagamento, QuantidadePassageiros, Data) VALUES
(1, 1, 'Economica', 'PIX', 1, '2025-11-10'),
(2, 2, 'Executiva', 'CREDITO', 2, '2025-11-12'),
(3, 3, 'Primeira Classe', 'DEBITO', 1, '2025-11-15'),
(4, 4, 'Economica', 'PIX', 3, '2025-11-18'),
(5, 5, 'Executiva', 'CREDITO', 2, '2025-11-20');


INSERT INTO Tripulacao (ID_voo) VALUES
(1),
(2),
(3),
(4),
(5);