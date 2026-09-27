// SPDX-License-Identifier: MIT
pragma solidity 0.8.19;

/**
 * MusicRegistry - Registro de obras da Fundacao DOP
 * Cada obra tem: id, nome, artista, hash do arquivo, preco
 * Tudo auditavel on-chain.
 */
contract MusicRegistry {

    struct Obra {
        uint256 id;
        string nome;
        string artista;
        string hashArquivo;
        uint256 preco;
        address dono;
        uint256 criadoEm;
    }

    Obra[] public obras;
    uint256 public totalObras;

    event ObraRegistrada(
        uint256 indexed id,
        string nome,
        string artista,
        address indexed dono
    );

    function registrar(
        string memory nome,
        string memory artista,
        string memory hashArquivo,
        uint256 preco
    ) public returns (uint256) {
        uint256 novoId = totalObras;

        Obra memory nova = Obra({
            id: novoId,
            nome: nome,
            artista: artista,
            hashArquivo: hashArquivo,
            preco: preco,
            dono: msg.sender,
            criadoEm: block.timestamp
        });

        obras.push(nova);
        totalObras++;

        emit ObraRegistrada(novoId, nome, artista, msg.sender);
        return novoId;
    }

    function obterObra(uint256 id) public view returns (
        uint256,
        string memory,
        string memory,
        string memory,
        uint256,
        address,
        uint256
    ) {
        require(id < totalObras, "Obra nao existe");
        Obra memory o = obras[id];
        return (
            o.id,
            o.nome,
            o.artista,
            o.hashArquivo,
            o.preco,
            o.dono,
            o.criadoEm
        );
    }

    function contar() public view returns (uint256) {
        return totalObras;
    }
}