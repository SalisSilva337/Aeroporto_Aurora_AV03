-- Tabela de Passageiro
CREATE TABLE Passageiro ( 
    ID_passageiro SERIAL PRIMARY KEY, 
    Nome VARCHAR(100) NOT NULL, 
    Email VARCHAR(100) UNIQUE NOT NULL, 
    Telefone VARCHAR(20) NOT NULL,
    Senha BYTEA NOT NULL
); 

-- Tabela de Reservas 
CREATE TABLE Reserva (
    ID_reserva SERIAL PRIMARY KEY,
    ID_passageiro INT NOT NULL,
    ID_voo INT NOT NULL,
    Classe VARCHAR(20) NOT NULL CHECK (Classe IN ('Economica', 'Executiva', 'Primeira Classe')),
    Metodo_Pagamento VARCHAR(50) NOT NULL CHECK (Metodo_Pagamento IN ('PIX', 'DEBITO', 'CREDITO')),
    Quantidade_Passageiros INT NOT NULL,
    Data DATE NOT NULL,
    FOREIGN KEY (ID_passageiro) REFERENCES Passageiro(ID_passageiro),
    FOREIGN KEY (ID_voo) REFERENCES Voo(ID_voo)
);

-- Tabela de Voo
CREATE TABLE Voo ( 
    ID_voo SERIAL PRIMARY KEY, 
    id_aviao int not null default(1), 
    Local_Partida VARCHAR(100) NOT NULL, 
    Local_Destino VARCHAR(100) NOT NULL, 
    Duracao INTERVAL NOT NULL,
    FOREIGN KEY (id_aviao) REFERENCES Aviao(ID_Aviao)
); 

-- Tabela de Aviao
CREATE TABLE Aviao (
    ID_Aviao SERIAL PRIMARY KEY,
    Modelo VARCHAR(100) NOT NULL,
    Capacidade INT NOT NULL
);

-- Tabela de Tripulação 
CREATE TABLE Tripulacao ( 
    ID_tripulacao SERIAL PRIMARY KEY, 
    ID_voo INT NOT NULL, 
    Pilotos INT NOT NULL DEFAULT(2), 
    Navegador INT NOT NULL DEFAULT(2), 
    Mecanico_Radio INT NOT NULL DEFAULT(2), 
    Comissarios_Bordo INT NOT NULL DEFAULT(3), 
    Mecanicos_Voo INT NOT NULL DEFAULT(4), 
    FOREIGN KEY (ID_voo) REFERENCES Voo(ID_voo) 
);