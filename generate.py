import os

def gen_global_alert():
    return """
        <div class="global-alert">
            <i class="fa-solid fa-circle-check global-alert-icon"></i>
            <div class="global-alert-content">
                <h2>Guía Definitiva - Proyecto Final Cisco (MIEMPRESA)</h2>
                <p>Basado en los laboratorios del curso y los requerimientos de la rúbrica oficial. Aprenderás paso a paso cómo configurar toda la topología en Packet Tracer, desde el VLSM hasta los servicios Cloud, utilizando el estándar de <strong>nuestro subnetting (10.19X.0.0/16)</strong>.</p>
            </div>
        </div>
"""

def gen_module_0():
    return """
        <section id="modulo-0" class="module-section">
            <div class="module-header">
                <span class="module-number">00</span>
                <h2 class="module-title">Troubleshooting y Comandos Básicos</h2>
            </div>
            <div class="card">
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-stethoscope"></i><span>Diagnóstico de Red (Comandos de Prueba)</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Aplica el proceso de solución de problemas (top-down, bottom-up o divide-and-conquer) según el <strong>Laboratorio 09c</strong>. Verifica siempre capa física (cables) antes que enrutamiento.</p>
                            <table class="data-table">
                                <tr>
                                    <th>Comando Completo</th>
                                    <th>Función Principal</th>
                                </tr>
                                <tr>
                                    <td><strong><span class="highlight-cyan">ping</span></strong> [ip-destino]</td>
                                    <td>Prueba de conectividad básica (ICMP). Si recibes <code>!</code>, es exitoso. Puntos (<code>.</code>) significan paquete perdido.</td>
                                </tr>
                                <tr>
                                    <td><strong><span class="highlight-cyan">tracert</span></strong> o <strong><span class="highlight-cyan">traceroute</span></strong></td>
                                    <td>Rastreo salto por salto para detectar dónde se rompe la red.</td>
                                </tr>
                                <tr>
                                    <td><strong><span class="highlight-cyan">show ip interface brief</span></strong></td>
                                    <td>Resumen del estado de puertos (UP/DOWN).</td>
                                </tr>
                                <tr>
                                    <td><strong><span class="highlight-cyan">show ip route</span></strong></td>
                                    <td>Muestra la tabla de enrutamiento (C para conectadas, S para estáticas, R para RIP).</td>
                                </tr>
                            </table>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-floppy-disk"></i><span>Configuración Básica de Switch y Router</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Según el <strong>Laboratorio 05a</strong>, todo equipo debe tener configuración básica de seguridad:</p>
                            <div class="code-block">
                                <span class="comment">! 1. Ingresar al modo privilegiado y configuración global</span>
                                <span class="code-line"><span class="cli-prompt">Switch></span> enable</span>
                                <span class="code-line"><span class="cli-prompt">Switch#</span> configure terminal</span>
                                <span class="comment">! 2. Asignar nombre (Ej: S1_LIMA)</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config)#</span> hostname S1_LIMA</span>
                                <span class="comment">! 3. Contraseña encriptada para el modo privilegiado</span>
                                <span class="code-line"><span class="cli-prompt">S1_LIMA(config)#</span> enable secret class</span>
                                <span class="comment">! 4. Mensaje de advertencia (Banner MOTD)</span>
                                <span class="code-line"><span class="cli-prompt">S1_LIMA(config)#</span> banner motd & Solo Acceso Autorizado &</span>
                                <span class="comment">! Guardar configuración (el atajo 'do' permite guardar desde config)</span>
                                <span class="code-line"><span class="cli-prompt">S1_LIMA(config)#</span> do write</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

def gen_module_1():
    return """
        <section id="modulo-1" class="module-section">
            <div class="module-header">
                <span class="module-number">01</span>
                <h2 class="module-title">Diseño Lógico IP y VLSM</h2>
            </div>
            <div class="card">
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-sitemap"></i><span>Subnetting para 5 Sedes</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Nuestra red corporativa usa el bloque <strong>10.19X.0.0/16</strong>. Según el <strong>Laboratorio 04 (FLSM/VLSM)</strong>, primero dividimos este gran bloque /16 en subredes más pequeñas para cada sede geográfica (Lima, La Libertad, Ica, Huánuco, Puno), y luego aplicamos VLSM internamente en cada sede.</p>
                            
                            <div class="alert-box info">
                                <i class="fa-solid fa-calculator"></i>
                                <div class="alert-box-content">
                                    <strong>Cálculo de Crecimiento (Rúbrica)</strong>
                                    <p>Antes de aplicar VLSM, debes sumar el <strong>25% de crecimiento proyectado a 10 años</strong> (para Lima) o el 20% para sucursales al total de hosts de cada departamento. ¡No calcules con los hosts actuales o te quedarás sin IPs en el futuro!</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-server"></i><span>La VLAN de Gestión (Fundamental)</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <div class="theory-box">
                                <h4>¿Cuántos hosts necesita Gestión?</h4>
                                <p>La VLAN de Gestión <strong>NO es un número al azar</strong>. Asigna 1 IP a CADA equipo de red (Routers, Switches Core/Multicapa, Switches de Acceso, Access Points) para administración por SSH.</p>
                                <p><strong>Fórmula:</strong> Suma todos los dispositivos de red + 1 (Para la PC-Admin) + % Crecimiento.</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-network-wired"></i><span>Enlaces WAN (Punto a Punto /30)</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <div class="alert-box">
                                <i class="fa-solid fa-triangle-exclamation"></i>
                                <div class="alert-box-content">
                                    <strong>La regla del /30 para enlaces WAN</strong>
                                    <p>Las conexiones entre Routers y entre el Core y el Router usan máscara <strong>255.255.255.252 (/30)</strong>. Esto otorga exactamente 2 IPs útiles (una para cada extremo del cable), evitando desperdicio de direcciones IP.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

def gen_module_2():
    return """
        <section id="modulo-2" class="module-section">
            <div class="module-header">
                <span class="module-number">02</span>
                <h2 class="module-title">Capa 2: VLANs y Enlaces Troncales</h2>
            </div>
            <div class="card">
                
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-layer-group"></i><span>Creación de VLANs y Puertos de Acceso</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Según el <strong>Laboratorio 05b</strong>, las VLANs segmentan el tráfico para mejorar el rendimiento y la seguridad. Esto se configura en los Switches de Acceso (Capa 2).</p>
                            <div class="code-block">
                                <span class="comment">! 1. Crear las VLANs en el Switch</span>
                                <span class="code-line"><span class="cli-prompt">SW_ACCESO(config)#</span> vlan 10</span>
                                <span class="code-line"><span class="cli-prompt">SW_ACCESO(config-vlan)#</span> name Administracion</span>
                                <span class="code-line"><span class="cli-prompt">SW_ACCESO(config-vlan)#</span> vlan 99</span>
                                <span class="code-line"><span class="cli-prompt">SW_ACCESO(config-vlan)#</span> name Nativa-Gestion</span>
                                <span class="code-line"><span class="cli-prompt">SW_ACCESO(config-vlan)#</span> exit</span>
                                <br>
                                <span class="comment">! 2. Asignar puertos a PCs (Modo Acceso)</span>
                                <span class="code-line"><span class="cli-prompt">SW_ACCESO(config)#</span> interface fastEthernet 0/2</span>
                                <span class="code-line"><span class="cli-prompt">SW_ACCESO(config-if)#</span> switchport mode access</span>
                                <span class="code-line"><span class="cli-prompt">SW_ACCESO(config-if)#</span> switchport access vlan 10</span>
                                <span class="code-line"><span class="cli-prompt">SW_ACCESO(config-if)#</span> exit</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-arrows-split-up-and-left"></i><span>Enlaces Troncales y VLAN Nativa</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Para que múltiples VLANs puedan viajar por un solo cable hacia el Switch Core, se usa un puerto troncal. Además, la rúbrica pide cambiar la VLAN nativa (por seguridad) de la 1 a la 99.</p>
                            <div class="code-block">
                                <span class="comment">! Configurar enlace hacia el Core como Troncal</span>
                                <span class="code-line"><span class="cli-prompt">SW_ACCESO(config)#</span> interface gigabitEthernet 0/1</span>
                                <span class="code-line"><span class="cli-prompt">SW_ACCESO(config-if)#</span> switchport mode trunk</span>
                                <span class="comment">! Cambiar VLAN nativa para mayor seguridad</span>
                                <span class="code-line"><span class="cli-prompt">SW_ACCESO(config-if)#</span> switchport trunk native vlan 99</span>
                                <span class="code-line"><span class="cli-prompt">SW_ACCESO(config-if)#</span> exit</span>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </section>
"""

def gen_module_3():
    return """
        <section id="modulo-3" class="module-section">
            <div class="module-header">
                <span class="module-number">03</span>
                <h2 class="module-title">El Núcleo L3: Enrutamiento Inter-VLAN</h2>
            </div>
            <div class="card">
                
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-microchip"></i><span>Switch Multicapa (Core) y SVIs</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">A diferencia del método "Router-on-a-stick", en este proyecto corporativo (según el trabajo de referencia y <strong>Laboratorio 05c</strong>) usamos Switches de Capa 3 (Multilayer) como Core en cada sede para enrutar el tráfico entre VLANs mediante <strong>SVIs (Switch Virtual Interfaces)</strong>.</p>
                            
                            <div class="alert-box info">
                                <i class="fa-solid fa-bolt"></i>
                                <div class="alert-box-content">
                                    <strong>Activación de Enrutamiento L3</strong>
                                    <p>Por defecto, un switch multicapa se comporta como un switch normal (Capa 2). Para que funcione como router y permita el paso entre VLANs, DEBES ejecutar el comando <strong><span class="highlight-cyan">ip routing</span></strong>.</p>
                                </div>
                            </div>

                            <div class="code-block">
                                <span class="comment">! CONFIGURACIÓN EN SWITCH CORE (Ej: CORE_LIMA)</span>
                                <span class="comment">! 1. Habilitar funciones de enrutamiento (Capa 3)</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> ip routing</span>
                                <br>
                                <span class="comment">! 2. Crear las VLANs primero en el Core</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> vlan 10</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-vlan)#</span> name Administracion</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-vlan)#</span> exit</span>
                                <br>
                                <span class="comment">! 3. Crear las SVIs (Puertas de enlace / Default Gateways de las PCs)</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> interface vlan 10</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> ip address 10.81.41.1 255.255.255.0</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> no shutdown</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> exit</span>
                                <br>
                                <span class="comment">! 4. Puerto ruteado hacia el Router Borde (No switchport)</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> interface gigabitEthernet 1/0/24</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> no switchport</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> ip address 10.81.40.2 255.255.255.252</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> no shutdown</span>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </section>
"""

def gen_module_4():
    return """
        <section id="modulo-4" class="module-section">
            <div class="module-header">
                <span class="module-number">04</span>
                <h2 class="module-title">Enlaces WAN y Autenticación PPP</h2>
            </div>
            <div class="card">
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-lock"></i><span>Encapsulamiento PPP y PAP vs CHAP</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <div class="theory-box">
                                <h4>Laboratorio 12: PAP y CHAP</h4>
                                <p>Por defecto, las interfaces seriales de Cisco usan encapsulamiento HDLC. La rúbrica exige cambiarlo a <strong>PPP</strong> para incorporar autenticación en los enlaces WAN (Hub and Spoke desde Lima hacia sucursales).</p>
                                <ul>
                                    <li><strong>PAP:</strong> Envía la contraseña en texto claro (2 pasos).</li>
                                    <li><strong>CHAP:</strong> Usa un desafío cifrado hash (3 pasos). Las contraseñas secretas en ambos routers deben coincidir.</li>
                                </ul>
                            </div>

                            <div class="code-block">
                                <span class="comment">! CONFIGURACIÓN CHAP (Ejemplo: Router_Lima hacia Router_Ica)</span>
                                <span class="comment">! 1. Crear usuario/clave cruzada en Router_Lima:</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config)#</span> username Router_Ica secret miclave123</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config)#</span> interface s0/0/0</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-if)#</span> encapsulation ppp</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-if)#</span> ppp authentication chap</span>
                                <br>
                                <span class="comment">! En el Router_Ica, creas la inversa:</span>
                                <span class="code-line"><span class="cli-prompt">Router_Ica(config)#</span> username Router_Lima secret miclave123</span>
                                <span class="code-line"><span class="cli-prompt">Router_Ica(config)#</span> interface s0/0/0</span>
                                <span class="code-line"><span class="cli-prompt">Router_Ica(config-if)#</span> encapsulation ppp</span>
                                <span class="code-line"><span class="cli-prompt">Router_Ica(config-if)#</span> ppp authentication chap</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

def gen_module_5():
    return """
        <section id="modulo-5" class="module-section">
            <div class="module-header">
                <span class="module-number">05</span>
                <h2 class="module-title">Enrutamiento RIPv2 y Failover Estático</h2>
            </div>
            <div class="card">
                
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-route"></i><span>RIPv2 (Enrutamiento Dinámico Interno)</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Según el <strong>Laboratorio 10</strong>, RIPv2 propaga automáticamente las rutas de todas nuestras VLANs entre sedes.</p>
                            <div class="code-block">
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config)#</span> router rip</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-router)#</span> version 2</span>
                                <span class="comment">! Declarar las redes principales conectadas (Clase A, B o C)</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-router)#</span> network 10.0.0.0</span>
                                <span class="comment">! Desactivar la sumarización automática (CRÍTICO para VLSM)</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-router)#</span> no auto-summary</span>
                                <span class="comment">! Redistribuir rutas estáticas (Para inyectar el acceso a Internet)</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-router)#</span> default-information originate</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-random"></i><span>Rutas Flotantes y Failover hacia Internet</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <div class="theory-box">
                                <h4>Laboratorio 09b: Rutas Estáticas Flotantes</h4>
                                <p>La rúbrica exige conexión a 2 ISPs. El ISP1 debe ser el principal, y el ISP2 actuará como respaldo (Failover). Para lograr esto, creamos una <strong>Ruta Estática Flotante</strong> dándole a la ruta hacia el ISP2 una <em>Distancia Administrativa (AD)</em> mayor (ej. 10).</p>
                            </div>
                            <div class="code-block">
                                <span class="comment">! Ruta principal (ISP1) - Distancia Administrativa 1 por defecto</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config)#</span> ip route 0.0.0.0 0.0.0.0 200.1.1.2</span>
                                <span class="comment">! Ruta de respaldo (ISP2) - Distancia Administrativa 10</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config)#</span> ip route 0.0.0.0 0.0.0.0 201.2.2.2 10</span>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </section>
"""

def gen_module_6():
    return """
        <section id="modulo-6" class="module-section">
            <div class="module-header">
                <span class="module-number">06</span>
                <h2 class="module-title">Servicios de Red (DHCP, DNS, WEB, FTP, Mail)</h2>
            </div>
            <div class="card">
                
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-server"></i><span>Implementación en Servidores Locales</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">El <strong>Laboratorio 11c</strong> explica la configuración gráfica de servidores en Packet Tracer.</p>
                            
                            <table class="data-table">
                                <tr>
                                    <th>Servicio</th>
                                    <th>Configuración Clave en Packet Tracer</th>
                                </tr>
                                <tr>
                                    <td><strong>DHCP</strong></td>
                                    <td>Pestaña <em>Services > DHCP</em>. Enciéndelo. Crea un "Pool" por cada VLAN (Ventas, Marketing, etc.). Define el Default Gateway (IP de la SVI), el DNS Server y la IP inicial. <strong>No olvides excluir las IPs de los servidores.</strong></td>
                                </tr>
                                <tr>
                                    <td><strong>DNS</strong></td>
                                    <td>Pestaña <em>Services > DNS</em>. Agrega un "A Record" mapeando dominios corporativos (ej. `www.lima.com`, `ftp.lima.com`, `mail.miempresa.com`) hacia sus respectivas IPs de servidores.</td>
                                </tr>
                                <tr>
                                    <td><strong>WEB (HTTP)</strong></td>
                                    <td>Pestaña <em>Services > HTTP</em>. Activa HTTP y HTTPS. Edita el archivo `index.html` del servidor para personalizar el portal de bienvenida corporativo.</td>
                                </tr>
                                <tr>
                                    <td><strong>FTP</strong></td>
                                    <td>Pestaña <em>Services > FTP</em>. Crea usuarios (ej. `adminLima`) y asígnales permisos de Lectura (R), Escritura (W), Eliminado (D), Renombrado (N) y Listado (L).</td>
                                </tr>
                                <tr>
                                    <td><strong>MAIL (SMTP/POP3)</strong></td>
                                    <td>Pestaña <em>Services > EMAIL</em>. Configura el Domain Name (ej. `peru.com`). Crea las cuentas de usuario con sus claves. Esto permitirá a las PCs usar la app <em>Mail Browser</em>.</td>
                                </tr>
                            </table>
                            
                            <div class="alert-box">
                                <i class="fa-solid fa-network-wired"></i>
                                <div class="alert-box-content">
                                    <strong>Laboratorio 11a y 11b: Análisis de Tráfico TCP/UDP</strong>
                                    <p>Verifica el funcionamiento usando el modo <em>Simulation</em> en Packet Tracer. Podrás observar el DNS usando <strong>UDP Port 53</strong>, Web usando <strong>TCP Port 80 (HTTP) y 443 (HTTPS)</strong> con su Three-Way Handshake (SYN, SYN-ACK, ACK), y el correo enviando vía <strong>SMTP (TCP 25)</strong> y recibiendo por <strong>POP3 (TCP 110)</strong>.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </section>
"""

def gen_module_7():
    return """
        <section id="modulo-7" class="module-section">
            <div class="module-header">
                <span class="module-number">07</span>
                <h2 class="module-title">Seguridad (Listas de Control de Acceso y SSH)</h2>
            </div>
            <div class="card">
                
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-shield-virus"></i><span>Las 5 Políticas de Seguridad (Rúbrica)</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">El <strong>Laboratorio 13 (ACLs)</strong> nos enseña a utilizar ACLs Extendidas (100-199) para filtrar por puerto y protocolo. En el Switch Multicapa Core de Lima, configuraremos una lista llamada `POLITICAS_LIMA`.</p>
                            
                            <div class="code-block">
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> ip access-list extended POLITICAS_LIMA</span>
                                <br>
                                <span class="comment">! Política 2: Web (Solo puertos 80 HTTP y 443 HTTPS)</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> permit tcp any any eq 80</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> permit tcp any any eq 443</span>
                                <br>
                                <span class="comment">! Política 3: DHCP (Solo puertos UDP 67 y 68)</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> permit udp any any eq 67</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> permit udp any any eq 68</span>
                                <br>
                                <span class="comment">! Política 4: Correo (SMTP 25 y POP3 110)</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> permit tcp any host 10.81.43.37 eq 25</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> permit tcp any host 10.81.43.37 eq 110</span>
                                <br>
                                <span class="comment">! Política 1: FTP Exclusivo local y hacia la Matriz (Puerto 21)</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> permit tcp any host 10.81.43.38 eq 21</span>
                                <br>
                                <span class="comment">! Permitir el resto del tráfico general (Ej. Ping ICMP)</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> permit ip any any</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> exit</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-user-shield"></i><span>Política 5: SSH Exclusivo para PC-ADMIN</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Garantizamos que solo la VLAN de Gestión pueda administrar los equipos mediante SSH.</p>
                            <div class="code-block">
                                <span class="comment">! 1. Crear una ACL Estándar que permita solo la IP de la PC-Admin</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> ip access-list standard ACL_GESTION</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-std-nacl)#</span> permit 10.81.42.192 0.0.0.31</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-std-nacl)#</span> deny any</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-std-nacl)#</span> exit</span>
                                <br>
                                <span class="comment">! 2. Aplicar la ACL a las líneas VTY de acceso remoto SSH</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> line vty 0 4</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-line)#</span> transport input ssh</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-line)#</span> login local</span>
                                <span class="comment">! El comando 'access-class' restringe quién puede hacer login</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-line)#</span> access-class ACL_GESTION in</span>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </section>
"""

def gen_module_8():
    return """
        <section id="modulo-8" class="module-section">
            <div class="module-header">
                <span class="module-number">08</span>
                <h2 class="module-title">Redes Inalámbricas (WLAN 802.11)</h2>
            </div>
            <div class="card">
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-wifi"></i><span>Configuración de Wireless Routers y APs</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">El <strong>Laboratorio 06</strong> indica que los <em>Access Points (AP)</em> son dispositivos de capa 2 que extienden la red, mientras que los <em>Wireless Routers</em> actúan en capa 3 con su propio NAT y DHCP.</p>
                            <div class="alert-box info">
                                <i class="fa-solid fa-signal"></i>
                                <div class="alert-box-content">
                                    <strong>Red Inalámbrica Segura</strong>
                                    <p>Para las sedes, utilizaremos Access Points conectados a los Switches. Se deben configurar dos SSIDs distintos (Ej. `WiFi_Clientes` y `WiFi_Ejecutivos`) usando autenticación <strong>WPA2-PSK</strong> con contraseñas seguras y asociando cada tráfico a sus VLANs respectivas.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

def gen_module_9():
    return """
        <section id="modulo-9" class="module-section">
            <div class="module-header">
                <span class="module-number">09</span>
                <h2 class="module-title">Solución Cloud y Backups (AWS)</h2>
            </div>
            <div class="card">
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-cloud"></i><span>Sustentación de Migración Cloud</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">El hito final de la rúbrica requiere proponer y sustentar una solución Cloud de Backups para MIEMPRESA. Hemos evaluado Azure, GCP y AWS, y se ha seleccionado <strong>Amazon Web Services (AWS)</strong>.</p>
                            
                            <table class="data-table">
                                <tr>
                                    <th>Servicio On-Premise</th>
                                    <th>Equivalente Propuesto en AWS</th>
                                </tr>
                                <tr>
                                    <td>Almacenamiento Local (Discos duros)</td>
                                    <td><strong>Amazon S3 (Simple Storage Service)</strong> con políticas de transición hacia S3 Glacier para archivos antiguos.</td>
                                </tr>
                                <tr>
                                    <td>Router Central</td>
                                    <td><strong>AWS Route Tables y NAT Gateway</strong></td>
                                </tr>
                                <tr>
                                    <td>Servidor WEB (Apache/Nginx local)</td>
                                    <td><strong>Amazon EC2</strong> (Elastic Compute Cloud) + Application Load Balancer</td>
                                </tr>
                                <tr>
                                    <td>Firewall Perimetral Físico</td>
                                    <td><strong>AWS Network Firewall</strong> y <strong>AWS WAF</strong> (Web Application Firewall)</td>
                                </tr>
                            </table>

                            <div class="alert-box info">
                                <i class="fa-solid fa-check"></i>
                                <div class="alert-box-content">
                                    <strong>Justificación Ténica (¿Por qué AWS?)</strong>
                                    <p>AWS proporciona integración nativa de sus servicios de Backup con AWS Storage. Ofrece durabilidad de 11 nueves (99.999999999%), replicación cruzada (Cross-Region Replication) y pago por uso (OPEX), lo que elimina los grandes costos iniciales (CAPEX) de comprar servidores físicos.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

def generate():
    content = ""
    content += gen_global_alert()
    content += gen_module_0()
    content += gen_module_1()
    content += gen_module_2()
    content += gen_module_3()
    content += gen_module_4()
    content += gen_module_5()
    content += gen_module_6()
    content += gen_module_7()
    content += gen_module_8()
    content += gen_module_9()
    return content

if __name__ == "__main__":
    with open("c:/Redes_Guia/main_content.html", "w", encoding="utf-8") as f:
        f.write(generate())

