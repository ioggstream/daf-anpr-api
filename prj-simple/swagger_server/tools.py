def get_index_doctypes(cli, index):
    mappings = cli.indices.get_mapping(index=index)
    return sorted(list(mappings[index]['mappings'].keys()))
