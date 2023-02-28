with open('NES_Connector_old.kicad_mod') as orig:
    with open('NES_Connector.kicad_mod', 'w') as fix:
        for line in orig:
            if '(pad "' in line:
                parts = line.split('"')
                if len(parts[1]) > 0:
                    if int(parts[1]) > 36:
                        # parts[1] = str(109 - int(parts[1]))
                        pass
                    else:
                        parts[1] = str(37 - int(parts[1]))
                line = '"'.join(parts)
            fix.write(line)
