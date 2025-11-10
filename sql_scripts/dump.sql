INSERT INTO Aviao (Modelo, Capacidade) VALUES
('Boeing 737-800', 189),
('Airbus A320neo', 180),
('Embraer E195-E2', 132),
('Boeing 777-300ER', 396),
('Airbus A350-900', 350);


INSERT INTO Voo (ID_voo, Local_Partida, Local_Destino, Disponibilidade, Duracao) VALUES
(1, 'São Paulo', 'Rio de Janeiro', TRUE, '01:10'),
(2, 'Brasília', 'Salvador', TRUE, '02:15'),
(3, 'Curitiba', 'Belo Horizonte', TRUE, '01:45'),
(4, 'Recife', 'Fortaleza', TRUE, '01:00'),
(5, 'Porto Alegre', 'Florianópolis', TRUE, '00:50');


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