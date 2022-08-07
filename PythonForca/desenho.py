def desenhaEnforcado(erros) -> None:
    match ( str(erros) ):
        case '1':
            print('\t O')
        case '2':
            print('\t O')
            print('\t ^',end='')
        case '3':
            print('\t O')
            print('\t/^',end='')
        case '4':
            print('\t O')
            print('\t/^\\')
        case '5':
            print('\t O')
            print('\t/^\\')
            print('\t |',end='')
        case '6':
            print('\t O')
            print('\t/^\\')
            print('\t| |')