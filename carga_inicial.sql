-- Script de Inicialização e Carga - Ferramentas WEB
-- Criação das tabelas + categorias + produtos

------------------------------------------------------------
-- 1. TABELA DE CATEGORIAS
------------------------------------------------------------
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

------------------------------------------------------------
-- 2. CARGA DE CATEGORIAS (UI)
------------------------------------------------------------
INSERT INTO categorias (name) VALUES ('Ferramentas Manuais');
INSERT INTO categorias (name) VALUES ('Elétricas');
INSERT INTO categorias (name) VALUES ('EPIs');
INSERT INTO categorias (name) VALUES ('Construção');
INSERT INTO categorias (name) VALUES ('Jardinagem');

------------------------------------------------------------
-- 3. TABELA DE PRODUTOS
------------------------------------------------------------
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    created_at TEXT
);

------------------------------------------------------------
-- 4. CARGA DE PRODUTOS (10 ITENS)
------------------------------------------------------------

INSERT INTO produtos (name, price, category, description, created_at) VALUES 
('Martelo de Garra', 35.90, 'Ferramentas Manuais', 'Martelo de ferro 20mm com cabo de madeira', '2026-06-21 09:14:00');

INSERT INTO produtos (name, price, category, description, created_at) VALUES 
('Chave de Fenda', 15.50, 'Ferramentas Manuais', 'Chave de fenda simples em aço', '2026-06-18 15:22:00');

INSERT INTO produtos (name, price, category, description, created_at) VALUES 
('Furadeira de Impacto', 299.90, 'Elétricas', 'Furadeira potente de 500W com maleta', '2026-05-30 11:05:00');

INSERT INTO produtos (name, price, category, description, created_at) VALUES 
('Alicate Universal', 25.00, 'Ferramentas Manuais', 'Alicate universal 8 polegadas com cabo isolado', '2026-06-25 18:40:00');

INSERT INTO produtos (name, price, category, description, created_at) VALUES 
('Esmerilhadeira Angular', 349.90, 'Elétricas', 'Esmerilhadeira angular de 4.1/2 polegadas 850W', '2026-07-02 07:55:00');

INSERT INTO produtos (name, price, category, description, created_at) VALUES 
('Trena Métrica 5m', 19.90, 'Construção', 'Trena métrica de 5 metros com trava automática', '2026-05-12 13:10:00');

INSERT INTO produtos (name, price, category, description, created_at) VALUES 
('Nível de Bolha', 29.90, 'Construção', 'Nível de alumínio de 12 polegadas com 3 bolhas', '2026-06-08 10:45:00');

INSERT INTO produtos (name, price, category, description, created_at) VALUES 
('Serra Tico-Tico', 219.00, 'Elétricas', 'Serra tico-tico 400W com controle de velocidade', '2026-07-01 16:20:00');

INSERT INTO produtos (name, price, category, description, created_at) VALUES 
('Jogo de Chaves Allen', 42.50, 'Ferramentas Manuais', 'Estojo com 9 chaves Allen abauladas de 1.5 a 10mm', '2026-05-27 08:33:00');

INSERT INTO produtos (name, price, category, description, created_at) VALUES 
('Multímetro Digital', 79.90, 'Elétricas', 'Multímetro portátil com visor digital e teste de diodo', '2026-06-29 21:05:00');