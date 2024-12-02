@app.route('/insert-user/<name>', methods=['GET'])
def add_user_from_route(name):
    """
    Adiciona um usuário ao banco de dados com valor enviado na URL.
    URL exemplo: /insert-user/Catarina
    """
    if not name:
        return jsonify({'message': 'Nome é obrigatório na URL'}), 400

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (name) VALUES (%s)', (name,))
            conn.commit()
            return jsonify({'message': f'Usuário {name} adicionado com sucesso!'}), 201
        except Error as e:
            print(f"Erro ao inserir usuário: {e}")
            return jsonify({'message': 'Erro ao inserir usuário'}), 500
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify({'message': 'Erro ao conectar ao banco de dados'}), 500
