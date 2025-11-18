INSERT INTO Passageiro (Nome, Email, Telefone, Senha) VALUES
('João Silva', 'joao@email.com', '119999999', '$2b$12$8jEExWMEvkpzUdi6oX8uMOPwz8j2sSsx1noHVyMsMTs7theE4tEmK'),
('Maria Souza', 'maria@email.com', '219888888', '$2b$12$wqU9gDLKLOzOHESR0WrP3OsTz4lsCH2invT07TN.eQv5MR.ka2/3C'),
('Carlos Lima', 'carlos@email.com', '319777777', '$2b$12$NuxUQ9CnhQz7HWVkHLyAYOnhkVB92hDA/o9RIPaozNYXk/rh0/leO'),
('Ana Pereira', 'ana@email.com', '419666666', '$2b$12$qGUsYhqoBzHKpSwrjBYQ9uoIdGPuSPTeM2B6VZK2myxgJA/lk/.cu'),
('Bruno Castro', 'bruno@email.com', '619555555', '$2b$12$g4kqxSaWzG7tmV3pT2zlce8HDbkPdlT/UzXOScd2D326O1V8.MHtm');

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


INSERT INTO Reserva (ID_passageiro, ID_voo, Classe, Metodo_Pagamento, Quantidade_Passageiros, Data) VALUES
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