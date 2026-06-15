import os

def gen_mod_02():
    return """
        <section id="modulo-2" class="module-section">
            <div class="module-header">
                <span class="module-number">02</span>
                <h2 class="module-title">Capa 2 - VLANs y Enlaces Troncales</h2>
            </div>
            <div class="card">
                
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-layer-group"></i><span>¿Qué es una VLAN y para qué sirve?</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Imagina que tienes un edificio con muchas oficinas y pasillos. Si no hay paredes, todos escuchan el ruido de todos (esto se llama un <strong>Dominio de Broadcast</strong> único). Las VLANs (Redes de Área Local Virtuales) son como paredes lógicas que separan a los diferentes departamentos (Ventas, Finanzas, Administración) para que el tráfico no se mezcle, mejorando el rendimiento y la seguridad.</p>
                            <p class="theory-text">Con las VLANs, puedes tener varias redes separadas LÓGICAMENTE usando el mismo switch FÍSICO.</p>
                            
                            <div class="alert-box">
                                <i class="fa-solid fa-triangle-exclamation"></i>
                                <div class="alert-box-content">
                                    <strong>¡ALERTA CRÍTICA! La diferencia entre VLAN Nativa y VLAN de Gestión</strong>
                                    <p>Muchos estudiantes confunden esto en las sustentaciones. ¡Aprende la diferencia!</p>
                                    <ul>
                                        <li><strong>VLAN 99 (Gestión):</strong> Es como la "oficina del administrador". <strong>SÍ recibe una dirección IP</strong>. Se usa para conectarte a los switches y routers por SSH y configurarlos de manera remota.</li>
                                        <li><strong>VLAN 999 (Nativa):</strong> Es como un "agujero negro". <strong>NO recibe dirección IP</strong>. Su único trabajo es capturar tráfico sin etiqueta (untagged traffic) en los cables troncales. Cambiamos la VLAN Nativa de la VLAN 1 (por defecto) a la 999 por pura medida de seguridad contra ataques de "VLAN hopping".</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-plug"></i><span>Paso a Paso: Crear VLANs y Asignar Puertos de Acceso</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Primero debemos enseñarle al Switch qué VLANs existen. Luego, debemos conectar los cables de las computadoras (PCs, impresoras, servidores) a los puertos y decirle al Switch "este puerto pertenece a esta VLAN". Un puerto que conecta a un equipo final se llama puerto de <strong>Acceso</strong>.</p>
                            
                            <div class="code-block">
                                <span class="comment">! 1. CREAR LAS VLANS (Ejemplo para un Switch de Acceso)</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config)#</span> vlan 10</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-vlan)#</span> name Ventas</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-vlan)#</span> vlan 20</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-vlan)#</span> name Administracion</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-vlan)#</span> vlan 30</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-vlan)#</span> name Finanzas</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-vlan)#</span> vlan 99</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-vlan)#</span> name Gestion</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-vlan)#</span> vlan 999</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-vlan)#</span> name Nativa</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-vlan)#</span> exit</span>
                                <br>
                                <span class="comment">! 2. ASIGNAR PUERTOS A LAS VLANS (Modo Acceso)</span>
                                <span class="comment">! Usamos 'interface range' para configurar varios puertos a la vez</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config)#</span> interface range fastEthernet 0/1 - 10</span>
                                <span class="comment">! Decimos que estos puertos van a equipos finales:</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-if-range)#</span> switchport mode <span class="highlight-cyan">access</span></span>
                                <span class="comment">! Metemos estos puertos en la VLAN 10 (Ventas):</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-if-range)#</span> switchport access <span class="highlight-cyan">vlan 10</span></span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-if-range)#</span> exit</span>
                                <br>
                                <span class="comment">! 3. CREAR LA SVI DE GESTIÓN PARA PODER ADMINISTRAR EL SWITCH</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config)#</span> interface vlan 99</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-if)#</span> ip address 10.192.11.195 255.255.255.224</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-if)#</span> no shutdown</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-if)#</span> exit</span>
                                <span class="comment">! El switch necesita una puerta de enlace para saber cómo salir de su red</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config)#</span> ip default-gateway 10.192.11.193</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-arrows-split-up-and-left"></i><span>Paso a Paso: Configurar Enlaces Troncales</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Si tenemos 5 VLANs en nuestro Switch de Acceso, ¿necesitamos 5 cables diferentes para llevar la información al Switch Principal (Core)? ¡No! Usamos un cable especial llamado <strong>Enlace Troncal (Trunk)</strong>. Es como una autopista con muchos carriles, donde el tráfico de TODAS las VLANs viaja mezclado, pero empaquetado (etiquetado) para no confundirse.</p>
                            
                            <div class="code-block">
                                <span class="comment">! CONFIGURACIÓN DEL PUERTO TRONCAL (Cable que va hacia otro Switch)</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config)#</span> interface gigabitEthernet 0/1</span>
                                <span class="comment">! Convertimos el puerto en modo Troncal:</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-if)#</span> switchport mode <span class="highlight-cyan">trunk</span></span>
                                <span class="comment">! Cambiamos la VLAN nativa a la 999 (por seguridad):</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-if)#</span> switchport trunk <span class="highlight-cyan">native vlan 999</span></span>
                                <span class="comment">! Opcional/Recomendado: Permitir solo las VLANs que necesitamos</span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-if)#</span> switchport trunk <span class="highlight-cyan">allowed vlan all</span></span>
                                <span class="code-line"><span class="cli-prompt">Switch(config-if)#</span> exit</span>
                            </div>

                            <div class="alert-box info">
                                <i class="fa-solid fa-lightbulb"></i>
                                <div class="alert-box-content">
                                    <strong>¡Cuidado con la VLAN Nativa!</strong>
                                    <p>Para que un enlace troncal funcione correctamente, <strong>AMBOS EXTREMOS del cable deben tener la misma VLAN nativa</strong>. Si en un switch pones la 999 y en el otro dejas la 1, Cisco te inundará la consola de mensajes de error de "Native VLAN Mismatch".</p>
                                </div>
                            </div>
                            
                            <table class="data-table">
                                <tr>
                                    <th>Comando de Verificación</th>
                                    <th>¿Qué hace?</th>
                                </tr>
                                <tr>
                                    <td><strong><span class="highlight-cyan">show vlan brief</span></strong></td>
                                    <td>Verifica que creaste las VLANs y muestra qué puertos de acceso están en cada una.</td>
                                </tr>
                                <tr>
                                    <td><strong><span class="highlight-cyan">show interfaces trunk</span></strong></td>
                                    <td>Verifica qué puertos son troncales, qué VLAN nativa usan y qué VLANs están permitidas por ellos.</td>
                                </tr>
                            </table>
                        </div>
                    </div>
                </div>

            </div>
        </section>

        <section id="modulo-3" class="module-section">
            <div class="module-header">
                <span class="module-number">03</span>
                <h2 class="module-title">El Núcleo L3 - Enrutamiento Inter-VLAN</h2>
            </div>
            <div class="card">
                
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-microchip"></i><span>¿Por qué necesitamos un Switch de Capa 3?</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Las VLANs separan el tráfico tan bien, que ahora la PC de Ventas (VLAN 10) <strong>NO puede comunicarse</strong> con la PC de Finanzas (VLAN 30). ¡Están en mundos distintos! Para que puedan hablar, necesitamos un intermediario que conecte esos mundos: un <strong>Router</strong>.</p>
                            <p class="theory-text">Existen dos formas de hacer esto:</p>
                            <ul>
                                <li><strong style="color:var(--accent-orange)">Router-on-a-stick:</strong> Se usa un Router físico tradicional con subinterfaces (Ej. Fa0/0.10, Fa0/0.20). Es fácil de hacer, pero todo el tráfico pasa por un solo cable y el router se convierte en un cuello de botella.</li>
                                <li><strong style="color:var(--accent-cyan)">Switch Multicapa (L3):</strong> Usamos un "Super Switch" que tiene el cerebro de un Router por dentro. Crea interfaces virtuales (SVIs) para cada VLAN y rutea a la velocidad de la luz por hardware. <strong>¡Esta es la forma Enterprise y la que exige este proyecto!</strong></li>
                            </ul>
                            
                            <div class="theory-box">
                                <h4>La Magia del "ip routing"</h4>
                                <p>Un Switch Multicapa, al sacarlo de su caja, funciona solo como un switch tonto de capa 2. Para despertar su cerebro de router, tienes que activar el comando maestro: <strong><span class="highlight-cyan">ip routing</span></strong>.</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-network-wired"></i><span>Paso a Paso: Configurar el Switch de Distribución (Con SVIs)</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Una <strong>SVI (Switch Virtual Interface)</strong> es una puerta de enlace virtual. Es la IP que pondremos en la configuración de Default Gateway de las PCs de los usuarios. Aquí está la configuración para el Switch Multicapa de Distribución en Lima.</p>
                            
                            <div class="code-block">
                                <span class="comment">! CONFIGURACIÓN DEL SWITCH DE DISTRIBUCIÓN (Ej: D1_LIMA)</span>
                                <span class="comment">! 1. Despertar el cerebro del router</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config)#</span> ip routing</span>
                                <br>
                                <span class="comment">! 2. Crear las VLANs que llegarán desde abajo</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config)#</span> vlan 10</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-vlan)#</span> name Ventas</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-vlan)#</span> vlan 20</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-vlan)#</span> name Admin</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-vlan)#</span> vlan 99</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-vlan)#</span> name Gestion</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-vlan)#</span> exit</span>
                                <br>
                                <span class="comment">! 3. Crear las SVIs (El Default Gateway de cada VLAN)</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config)#</span> interface <span class="highlight-cyan">vlan 10</span></span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-if)#</span> ip address <span class="highlight-orange">10.192.8.1 255.255.255.0</span></span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-if)#</span> no shutdown</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-if)#</span> exit</span>
                                <br>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config)#</span> interface <span class="highlight-cyan">vlan 20</span></span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-if)#</span> ip address <span class="highlight-orange">10.192.9.1 255.255.255.128</span></span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-if)#</span> no shutdown</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-if)#</span> exit</span>
                                <br>
                                <span class="comment">! 4. Configurar el puerto que va HACIA ARRIBA (Al Core) como PUERTO RUTEADO</span>
                                <span class="comment">! 'no switchport' quita la funcion de capa 2 y permite ponerle una IP directa</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config)#</span> interface gigabitEthernet 1/0/24</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-if)#</span> <span class="highlight-cyan">no switchport</span></span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-if)#</span> ip address 172.16.0.2 255.255.255.252</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-if)#</span> no shutdown</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-if)#</span> exit</span>
                                <br>
                                <span class="comment">! 5. No olvides configurar el RIPv2 para anunciar estas redes</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config)#</span> router rip</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-router)#</span> version 2</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-router)#</span> no auto-summary</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-router)#</span> network 10.0.0.0</span>
                                <span class="code-line"><span class="cli-prompt">D1_LIMA(config-router)#</span> network 172.16.0.0</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-server"></i><span>Paso a Paso: Configurar el Switch Core Central</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">El Core Central L3 es como el gran jefe de Lima. Su única misión es rutear paquetes a la velocidad de la luz. <strong>El Core NO TIENE PCs conectadas, por lo que NO tiene VLANs de usuarios, ni necesita SVIs.</strong> Solo tiene puertos ruteados punto a punto (/30).</p>
                            
                            <div class="code-block">
                                <span class="comment">! CONFIGURACIÓN DEL SWITCH CORE CENTRAL (CORE_LIMA)</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> ip routing</span>
                                <br>
                                <span class="comment">! 1. Puertos hacia los Switches de Distribución (D1, D2, D3)</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> interface gigabitEthernet 1/0/1</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> <span class="highlight-cyan">no switchport</span></span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> ip address 172.16.0.1 255.255.255.252</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> no shutdown</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> exit</span>
                                <br>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> interface gigabitEthernet 1/0/2</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> <span class="highlight-cyan">no switchport</span></span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> ip address 172.16.0.5 255.255.255.252</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> no shutdown</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> exit</span>
                                <br>
                                <span class="comment">! 2. Puerto HACIA ARRIBA (Hacia el Router Perimetral 2911)</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> interface gigabitEthernet 1/0/24</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> <span class="highlight-cyan">no switchport</span></span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> ip address 172.16.0.13 255.255.255.252</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> no shutdown</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> exit</span>
                                <br>
                                <span class="comment">! 3. Activar RIPv2</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> router rip</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-router)#</span> version 2</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-router)#</span> no auto-summary</span>
                                <span class="comment">! Solo anunciamos las redes de interconexión 172.16.x.x, ya que no hay PCs locales</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-router)#</span> network 172.16.0.0</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-diagram-project"></i><span>Resumen Visual: ¿Quién conecta con quién?</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <div class="theory-box">
                                <h4>El Flujo del Tráfico en la Red Corporativa</h4>
                                <p>Visualiza el camino que toma la información desde la computadora del empleado hasta la salida de la sede:</p>
                                <ul>
                                    <li><strong>1. PC:</strong> Conectada al Switch de Acceso.</li>
                                    <li><strong>2. Switch de Acceso L2:</strong> No rutea. Recoge los cables de las PCs y agrupa las VLANs en un <strong>enlace troncal</strong> hacia arriba.</li>
                                    <li><strong>3. Switch de Distribución L3:</strong> Recibe el troncal. Tiene las <strong>SVIs (Gateways)</strong> de las PCs. Rutea el tráfico entre VLANs. Sale hacia el Core usando un <strong>puerto ruteado (/30)</strong>.</li>
                                    <li><strong>4. Switch Core Central L3:</strong> Recibe cables ruteados de todos los Switches de Distribución. Su trabajo es enrutar a toda velocidad. Sale hacia el Router Perimetral con otro <strong>puerto ruteado (/30)</strong>.</li>
                                    <li><strong>5. Router 2911:</strong> Frontera de la sede. Recibe tráfico del Core L3 y decide si lo envía por los enlaces seriales WAN hacia otras sedes, o si lo lanza a Internet.</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </section>

        <section id="modulo-4" class="module-section">
            <div class="module-header">
                <span class="module-number">04</span>
                <h2 class="module-title">Enlaces WAN y Autenticación PPP (PAP y CHAP)</h2>
            </div>
            <div class="card">
                
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-globe"></i><span>¿Qué es un enlace WAN y qué es PPP?</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text"><strong>WAN (Wide Area Network):</strong> Son redes inmensas. Sirven para unir nuestras sucursales geográficamente lejanas. En nuestro proyecto, Lima está en el centro conectada hacia Ica, La Libertad, Huánuco y Puno mediante cables seriales rojos (Topología Hub-and-Spoke).</p>
                            <p class="theory-text">Por defecto, cuando conectas un cable serial en Cisco, el idioma de empaquetado (encapsulamiento) de los datos es HDLC. Sin embargo, para mayor seguridad, usamos el protocolo <strong>PPP (Point-to-Point Protocol)</strong>. PPP envuelve los datos y añade una capa de autenticación, es decir, ¡pide usuario y contraseña antes de permitir que la otra sede se conecte!</p>
                            
                            <div class="theory-box">
                                <h4>DCE vs DTE (El Relojito)</h4>
                                <p>En los cables seriales viejos, un lado del cable manda (DCE) y el otro obedece (DTE). El lado DCE tiene un ícono de un pequeño reloj rojo en Packet Tracer. Ese lado <strong>debe dictar la velocidad</strong> usando el comando <code>clock rate 64000</code> en la interfaz serial.</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-unlock-keyhole"></i><span>PAP: Autenticación Simple (Texto Plano)</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text"><strong>PAP (Password Authentication Protocol):</strong> Es un método básico y de 2 pasos. Funciona como mostrarle tu DNI a un guardia en la puerta. El problema es que envía tu clave "desnuda" por la red, así que un hacker podría verla. La rúbrica nos pide implementar ambos métodos, PAP y CHAP. Aquí tienes cómo se configura PAP.</p>
                            
                            <div class="alert-box info">
                                <i class="fa-solid fa-lightbulb"></i>
                                <div class="alert-box-content">
                                    <strong>¡El Patrón Cruzado!</strong>
                                    <p>Para la autenticación, cada Router debe tener guardado en su base de datos el nombre del <strong>Router Vecino</strong> como usuario, y la contraseña debe ser la misma.</p>
                                </div>
                            </div>

                            <div class="code-block">
                                <span class="comment">! CONFIGURACIÓN PAP (Ejemplo: Enlace entre Lima e Ica)</span>
                                <span class="comment">! ---- EN ROUTER_LIMA ----</span>
                                <span class="comment">! 1. Crear el usuario del vecino</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config)#</span> username Router_Ica secret miclave123</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config)#</span> interface s0/0/0</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-if)#</span> ip address 172.16.1.1 255.255.255.252</span>
                                <span class="comment">! Si es el lado DCE, poner el reloj:</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-if)#</span> clock rate 64000</span>
                                <span class="comment">! 2. Cambiar de HDLC a PPP y activar PAP</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-if)#</span> encapsulation <span class="highlight-cyan">ppp</span></span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-if)#</span> ppp authentication <span class="highlight-cyan">pap</span></span>
                                <span class="comment">! 3. CRÍTICO: Mandarle TÚ usuario y TÚ clave al vecino para que te deje entrar</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-if)#</span> ppp pap sent-username <span class="highlight-orange">Router_Lima</span> password <span class="highlight-orange">miclave123</span></span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-if)#</span> no shutdown</span>
                                <br>
                                <span class="comment">! ---- EN ROUTER_ICA (El Espejo) ----</span>
                                <span class="code-line"><span class="cli-prompt">Router_Ica(config)#</span> username Router_Lima secret miclave123</span>
                                <span class="code-line"><span class="cli-prompt">Router_Ica(config)#</span> interface s0/0/0</span>
                                <span class="code-line"><span class="cli-prompt">Router_Ica(config-if)#</span> ip address 172.16.1.2 255.255.255.252</span>
                                <span class="code-line"><span class="cli-prompt">Router_Ica(config-if)#</span> encapsulation <span class="highlight-cyan">ppp</span></span>
                                <span class="code-line"><span class="cli-prompt">Router_Ica(config-if)#</span> ppp authentication <span class="highlight-cyan">pap</span></span>
                                <span class="code-line"><span class="cli-prompt">Router_Ica(config-if)#</span> ppp pap sent-username <span class="highlight-orange">Router_Ica</span> password <span class="highlight-orange">miclave123</span></span>
                                <span class="code-line"><span class="cli-prompt">Router_Ica(config-if)#</span> no shutdown</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-lock-open"></i><span>CHAP: Autenticación Segura (Cifrada)</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text"><strong>CHAP (Challenge Handshake Authentication Protocol):</strong> Es un método seguro de 3 pasos. Funciona como un agente secreto que te da un acertijo, lo resuelves con tu clave, y solo envías la respuesta. La clave secreta <strong>NUNCA viaja por el cable</strong>, lo que hace imposible que un hacker la robe. CHAP es más inteligente y automático que PAP.</p>
                            
                            <div class="code-block">
                                <span class="comment">! CONFIGURACIÓN CHAP (Ejemplo: Enlace entre Lima y La Libertad)</span>
                                <span class="comment">! ---- EN ROUTER_LIMA ----</span>
                                <span class="comment">! 1. Crear el usuario del vecino. (¡OJO! Sensible a mayúsculas y minúsculas)</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config)#</span> username Router_LaLibertad secret miclave123</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config)#</span> interface s0/0/1</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-if)#</span> encapsulation <span class="highlight-cyan">ppp</span></span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-if)#</span> ppp authentication <span class="highlight-cyan">chap</span></span>
                                <span class="comment">! (¡No necesitas el comando sent-username! CHAP lo hace solo)</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-if)#</span> no shutdown</span>
                                <br>
                                <span class="comment">! ---- EN ROUTER_LALIBERTAD ----</span>
                                <span class="code-line"><span class="cli-prompt">Router_LaLibertad(config)#</span> username Router_Lima secret miclave123</span>
                                <span class="code-line"><span class="cli-prompt">Router_LaLibertad(config)#</span> interface s0/0/1</span>
                                <span class="code-line"><span class="cli-prompt">Router_LaLibertad(config-if)#</span> encapsulation <span class="highlight-cyan">ppp</span></span>
                                <span class="code-line"><span class="cli-prompt">Router_LaLibertad(config-if)#</span> ppp authentication <span class="highlight-cyan">chap</span></span>
                                <span class="code-line"><span class="cli-prompt">Router_LaLibertad(config-if)#</span> no shutdown</span>
                            </div>

                            <div class="alert-box">
                                <i class="fa-solid fa-triangle-exclamation"></i>
                                <div class="alert-box-content">
                                    <strong>¿Mi línea serial se quedó en "down"?</strong>
                                    <p>Si la interfaz no levanta al usar PPP, verifica 3 cosas en orden: 1. ¿Tienen ambos lados 'encapsulation ppp'? (No puedes mezclar HDLC de un lado y PPP del otro). 2. ¿La contraseña es exactamente igual en ambos lados? 3. ¿El 'username' que pusiste coincide letra por letra con el 'hostname' configurado en el otro router?</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-scale-balanced"></i><span>¿Cuándo usar PAP y cuándo CHAP?</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">La rúbrica indica explícitamente: "<strong>Configurar autenticación PAP/CHAP en los enlaces Seriales.</strong>". Esto significa que debes demostrar que sabes hacer AMBOS.</p>
                            <p class="theory-text"><strong>Mi recomendación de diseño:</strong> Aplica CHAP para las conexiones principales como Lima-LaLibertad y Lima-Huánuco, y aplica PAP para Lima-Ica y Lima-Puno. Así, cuando expongas, podrás mostrar ambos métodos operando en la misma red sin problemas.</p>
                        </div>
                    </div>
                </div>

            </div>
        </section>
"""

def gen_mod_03():
    return """
        <section id="modulo-5" class="module-section">
            <div class="module-header">
                <span class="module-number">05</span>
                <h2 class="module-title">Enrutamiento Dinámico RIPv2 y Failover con Ruta Estática</h2>
            </div>
            <div class="card">
                
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-route"></i><span>¿Qué es el enrutamiento y por qué lo necesitamos?</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Imagina que un router es un cartero. Si le entregas un paquete para enviarlo a Ica, pero él solo conoce las calles de Lima, no sabrá qué hacer y descartará el paquete. El enrutamiento es el proceso de construirle un "mapa de calles" (Tabla de Enrutamiento) al router.</p>
                            <ul>
                                <li><strong>Enrutamiento Estático:</strong> El administrador de red escribe a mano cada ruta hacia cada destino. Seguro, pero pesado si hay muchas redes.</li>
                                <li><strong>Enrutamiento Dinámico:</strong> Los routers se cuentan chismes. Se dicen entre ellos "Oye, yo conozco la red de Ica, te la paso". Usamos <strong>RIPv2</strong> en este proyecto porque es lo que enseñan los laboratorios, es fácil de usar y propaga solita toda nuestra red.</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-arrows-turn-to-dots"></i><span>Paso a Paso: Configurar RIPv2 en los Routers</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Debemos decirle al router qué redes locales conoce para que empiece a propagarlas hacia las demás sedes.</p>
                            
                            <div class="code-block">
                                <span class="comment">! CONFIGURACIÓN RIPV2 (Ejemplo: Router_Lima)</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config)#</span> router rip</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-router)#</span> version 2</span>
                                <span class="comment">! CRÍTICO: ¡Desactivar el resumen automático!</span>
                                <span class="comment">! Sin esto, RIP agrupará tus subredes pequeñitas y DESTRUIRÁ todo tu diseño VLSM</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-router)#</span> <span class="highlight-cyan">no auto-summary</span></span>
                                <br>
                                <span class="comment">! Declarar las redes. ¡Ojo! Tienes que poner la red base (Clase A, B o C), no las subredes de VLSM.</span>
                                <span class="comment">! Aquí declaras la red que va a tus oficinas:</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-router)#</span> network <span class="highlight-orange">10.0.0.0</span></span>
                                <span class="comment">! Aquí declaras los enlaces WAN e interconexión:</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-router)#</span> network <span class="highlight-orange">172.16.0.0</span></span>
                                <br>
                                <span class="comment">! CRÍTICO: Esto hace que el Router_Lima les avise a todos "Si no saben a dónde ir, mándenme todo a mí, yo tengo salida a Internet"</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-router)#</span> <span class="highlight-cyan">default-information originate</span></span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config-router)#</span> exit</span>
                            </div>

                            <p class="theory-text">Para comprobar que todo funcionó, ve a Ica y ejecuta <strong><span class="highlight-cyan">show ip route</span></strong>. Si ves líneas que empiezan con una <strong><span class="highlight-orange">R</span></strong>, significa que Ica ya aprendió cómo llegar a Lima, La Libertad, etc. Si ves una <strong><span class="highlight-orange">R*</span></strong>, significa que aprendió la salida al Internet inyectada por el router Lima.</p>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-random"></i><span>Failover: Rutas Estáticas Flotantes (2 ISPs)</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">La rúbrica indica que la sede central debe conectarse a Internet a través de dos Proveedores de Servicio (ISP1 e ISP2). El ISP1 será el enlace principal, y si este se cae (falla el cable), la red debe enrutar automáticamente el tráfico por el ISP2 (Respaldo). A esto se le llama <strong>Failover</strong>, y según el <strong>Laboratorio 09b</strong>, se logra con Rutas Estáticas Flotantes.</p>
                            
                            <div class="theory-box">
                                <h4>La Distancia Administrativa (AD)</h4>
                                <p>Cisco prefiere las rutas con la menor Distancia Administrativa. Una ruta estática normal tiene AD = 1. Si creamos otra ruta estática igual, pero le damos AD = 10, esa ruta se quedará oculta (flotando) y solo aparecerá si la ruta de AD 1 desaparece (se corta el cable).</p>
                            </div>
                            
                            <div class="code-block">
                                <span class="comment">! CONFIGURACIÓN FAILOVER (En Router Perimetral de Lima)</span>
                                <span class="comment">! 1. Crear ruta estática principal por defecto hacia ISP1 (AD=1 por defecto)</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config)#</span> ip route 0.0.0.0 0.0.0.0 <span class="highlight-orange">200.1.1.2</span></span>
                                <br>
                                <span class="comment">! 2. Crear ruta estática flotante hacia ISP2 (Le asignamos AD=10 al final)</span>
                                <span class="code-line"><span class="cli-prompt">Router_Lima(config)#</span> ip route 0.0.0.0 0.0.0.0 <span class="highlight-orange">201.2.2.2</span> <span class="highlight-cyan">10</span></span>
                            </div>

                            <p class="theory-text"><strong>Prueba en Packet Tracer:</strong> Haz un ping constante desde una PC a Internet. Ve al Router y apaga (`shutdown`) la interfaz serial que va al ISP1. Verás cómo los pings fallan unos segundos y luego vuelven a responder, ¡porque la red saltó automáticamente al ISP2!</p>
                        </div>
                    </div>
                </div>

            </div>
        </section>

        <section id="modulo-6" class="module-section">
            <div class="module-header">
                <span class="module-number">06</span>
                <h2 class="module-title">Servicios de Red (DHCP, DNS, WEB, FTP, Correo)</h2>
            </div>
            <div class="card">
                
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-laptop-code"></i><span>DHCP: Asignación Automática de IPs</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">En vez de ir computadora por computadora colocando la IP estática (aburridísimo y propenso a errores), un servidor DHCP alquila IPs de manera automática.</p>
                            
                            <div class="theory-box">
                                <h4>Paso a Paso en Packet Tracer</h4>
                                <ol>
                                    <li>Haz clic en el Servidor y ve a la pestaña <strong>Services > DHCP</strong>.</li>
                                    <li>Enciende (<strong>Turn ON</strong>) el servicio.</li>
                                    <li>Crea un "Pool" (grupo de direcciones) para cada VLAN (Ej: Pool_Ventas, Pool_Marketing).</li>
                                    <li>En <strong>Default Gateway</strong> pon la IP de la SVI de esa VLAN (Ej: 10.192.8.1).</li>
                                    <li>En <strong>DNS Server</strong> pon la IP de tu servidor DNS principal.</li>
                                    <li>En <strong>Start IP Address</strong>, no empieces en la .1 porque esa es del gateway. Empieza en la .10 para dejar espacio para IPs estáticas de impresoras o servers.</li>
                                    <li>Dale a <strong>Add</strong>. Luego ve a cada PC > Desktop > IP Configuration > Selecciona DHCP.</li>
                                </ol>
                            </div>
                            
                            <div class="alert-box">
                                <i class="fa-solid fa-triangle-exclamation"></i>
                                <div class="alert-box-content">
                                    <strong>¿El DHCP no funciona (aparece 169.254.x.x APIPA)?</strong>
                                    <p>Revisa que el Default Gateway que configuraste en el Pool coincida EXACTAMENTE con la IP de la SVI configurada en el Switch Core Multicapa. Revisa también que la PC y el servidor DHCP estén en la misma VLAN o exista un "ip helper-address" configurado.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-magnifying-glass-location"></i><span>DNS: Traducir nombres a IPs</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Los humanos somos malos recordando números (IPs), pero buenos recordando nombres (www.google.com). El servidor <strong>DNS (Domain Name System)</strong> es como un directorio telefónico que traduce el nombre a una IP. Usa el protocolo <strong>UDP puerto 53</strong>.</p>
                            
                            <div class="theory-box">
                                <h4>Paso a Paso en Packet Tracer</h4>
                                <ol>
                                    <li>Haz clic en el Servidor DNS > <strong>Services > DNS</strong>. Enciéndelo (<strong>ON</strong>).</li>
                                    <li>En <strong>Name</strong> escribe el nombre deseado (Ej: <code>www.miempresa.com</code>).</li>
                                    <li>Asegúrate de que <strong>Type</strong> sea "A Record".</li>
                                    <li>En <strong>Address</strong> pon la IP del servidor WEB.</li>
                                    <li>Dale a <strong>Add</strong>. Repite esto para <code>ftp.miempresa.com</code> y <code>mail.miempresa.com</code>.</li>
                                    <li>Asegúrate de que tus PCs por DHCP reciban la IP de este servidor DNS.</li>
                                </ol>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-globe"></i><span>Servidor WEB (HTTP/HTTPS)</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Aloja la página corporativa que visitan tus sedes. Utiliza <strong>TCP puerto 80 (HTTP)</strong> y <strong>TCP puerto 443 (HTTPS)</strong>.</p>
                            
                            <div class="theory-box">
                                <h4>Paso a Paso en Packet Tracer</h4>
                                <ol>
                                    <li>Haz clic en el Servidor WEB > <strong>Services > HTTP</strong>. Enciende ambos, HTTP y HTTPS.</li>
                                    <li>Haz clic en <strong>edit</strong> en el archivo <code>index.html</code>.</li>
                                    <li>Cambia el código HTML para que diga "Bienvenidos a la Intranet de MIEMPRESA".</li>
                                    <li>Para probar, ve a una PC > Desktop > Web Browser y escribe <code>www.miempresa.com</code>.</li>
                                </ol>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-folder-tree"></i><span>Servidor FTP (Transferencia de Archivos)</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Permite subir, bajar y eliminar archivos en un repositorio central. Utiliza los <strong>puertos TCP 20 (para los datos) y 21 (para el control de la conexión)</strong>.</p>
                            
                            <div class="theory-box">
                                <h4>Paso a Paso en Packet Tracer</h4>
                                <ol>
                                    <li>Servidor FTP > <strong>Services > FTP</strong>. Enciéndelo.</li>
                                    <li>Crea un usuario (Ej: <code>adminLima</code>) y contraseña (Ej: <code>cisco123</code>).</li>
                                    <li>Marca las casillas de permisos según lo que puedan hacer: Read (Lectura), Write (Escritura), Delete (Eliminar), Rename (Renombrar), List (Listar).</li>
                                    <li>Dale a <strong>Add</strong> (+).</li>
                                    <li>Para probar, ve a una PC > Command Prompt > escribe <code>ftp ftp.miempresa.com</code>.</li>
                                </ol>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-envelope"></i><span>Servidor de Correo (SMTP/POP3)</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">El correo electrónico requiere de dos protocolos para funcionar. <strong>SMTP (TCP puerto 25)</strong> se encarga de ENVIAR el correo desde la PC al servidor. <strong>POP3 (TCP puerto 110)</strong> se encarga de DESCARGAR el correo desde el servidor a tu PC.</p>
                            
                            <div class="theory-box">
                                <h4>Paso a Paso en Packet Tracer</h4>
                                <ol>
                                    <li>Servidor de Correo > <strong>Services > EMAIL</strong>. Enciende SMTP y POP3.</li>
                                    <li>En <strong>Domain Name</strong>, escribe <code>miempresa.com</code> y pulsa <strong>Set</strong>.</li>
                                    <li>En <strong>User Setup</strong>, crea usuarios (Ej: <code>usuarioLima1</code> y <code>usuarioIca1</code>) con contraseñas y dales a Add (+).</li>
                                    <li>Ve a una PC > Desktop > Email > Configure Mail. Llena los datos con la info de <code>usuarioLima1@miempresa.com</code> y usa el DNS `mail.miempresa.com` como servidor de entrada y salida.</li>
                                    <li>Envía un correo de prueba a <code>usuarioIca1@miempresa.com</code>.</li>
                                </ol>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </section>

        <section id="modulo-7" class="module-section">
            <div class="module-header">
                <span class="module-number">07</span>
                <h2 class="module-title">Políticas de Seguridad (ACLs) y Acceso SSH</h2>
            </div>
            <div class="card">
                
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-shield-halved"></i><span>¿Qué es una ACL? (Explicación para principiantes)</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Una <strong>Lista de Control de Acceso (ACL)</strong> es como el guardia de seguridad VIP de una discoteca. Se planta en la puerta de un puerto del router, revisa cada paquete que intenta entrar o salir, mira su lista de reglas, y decide si lo deja pasar (<strong>permit</strong>) o lo descarta (<strong>deny</strong>).</p>
                            <p class="theory-text">El guardia lee la lista en estricto <strong>orden</strong>, de arriba a abajo. En cuanto encuentra una regla que coincide con el paquete, actúa y deja de leer el resto. Al final de TODA lista existe una regla invisible llamada <strong>"Deny Any" (Denegar Todo)</strong>. Si un paquete no coincide con ninguna regla permitida... ¡pam! El guardia lo rechaza y lo bota.</p>
                            
                            <table class="data-table">
                                <tr>
                                    <th>Tipo de ACL</th>
                                    <th>Número</th>
                                    <th>¿Qué pueden revisar?</th>
                                </tr>
                                <tr>
                                    <td><strong>Estándar</strong></td>
                                    <td>1 al 99</td>
                                    <td>Son básicas. Solo revisan de DÓNDE viene el paquete (IP Origen).</td>
                                </tr>
                                <tr>
                                    <td><strong>Extendida</strong></td>
                                    <td>100 al 199</td>
                                    <td>Son expertas. Revisan Origen, Destino, Protocolo (TCP/UDP) y el PUERTO. Son las que pide la rúbrica.</td>
                                </tr>
                            </table>

                            <div class="alert-box info">
                                <i class="fa-solid fa-mask"></i>
                                <div class="alert-box-content">
                                    <strong>La Máscara Wildcard (El gemelo malvado)</strong>
                                    <p>Las ACLs no usan la máscara de subred (ej. 255.255.255.0), usan una máscara Wildcard, que es exactamente la inversa. Un 0 significa "el número debe coincidir exactamente", un 255 significa "no me importa, deja pasar lo que sea". Ejemplo: <code>0.0.0.255</code> equivale a toda una red /24. Para un host específico (una PC), se usa <code>0.0.0.0</code> o la palabra <code>host</code>.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-list-check"></i><span>Las 5 Políticas de Seguridad del Proyecto</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">La rúbrica es clara, y el <strong>Laboratorio 13</strong> nos enseña a aplicarlo. Vamos a crear una gran <strong>ACL Extendida Nombrada</strong> en el Switch Core Multicapa de Lima.</p>

                            <div class="theory-box">
                                <h4>La Lógica de nuestras Políticas:</h4>
                                <ol>
                                    <li><strong>FTP Restringido:</strong> Solo se llega al servidor FTP (IP 10.81.43.38 en tu caso) por el puerto TCP 21.</li>
                                    <li><strong>Tráfico Web:</strong> Permitir tráfico de páginas web (TCP 80 HTTP y TCP 443 HTTPS).</li>
                                    <li><strong>DHCP Controlado:</strong> Permitir tráfico de DHCP (UDP 67 al servidor, UDP 68 al cliente).</li>
                                    <li><strong>Correo Exclusivo:</strong> Permitir acceso al servidor de Correo (IP 10.81.43.37) usando puertos SMTP (TCP 25) y POP3 (TCP 110).</li>
                                    <li><strong>SSH Exclusivo (VLAN Gestión):</strong> Bloquearemos cualquier intento de acceder a administrar los equipos, EXCEPTO a la PC-Admin de Gestión (esto lo haremos con una ACL especial abajo).</li>
                                </ol>
                            </div>

                            <div class="code-block">
                                <span class="comment">! CREACIÓN DE LA LISTA EXTENDIDA EN EL CORE L3</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> ip access-list extended <span class="highlight-cyan">POLITICAS_LIMA</span></span>
                                <br>
                                <span class="comment">! 1. Aplicamos Política FTP (Puerto 21)</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> permit tcp any host 10.81.43.38 eq <span class="highlight-orange">21</span></span>
                                <br>
                                <span class="comment">! 2. Aplicamos Política Web (Puertos 80 y 443)</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> permit tcp any any eq <span class="highlight-orange">80</span></span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> permit tcp any any eq <span class="highlight-orange">443</span></span>
                                <br>
                                <span class="comment">! 3. Aplicamos Política DHCP (Puertos 67 y 68)</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> permit udp any any eq <span class="highlight-orange">67</span></span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> permit udp any any eq <span class="highlight-orange">68</span></span>
                                <br>
                                <span class="comment">! 4. Aplicamos Política Mail (Puertos 25 y 110)</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> permit tcp any host 10.81.43.37 eq <span class="highlight-orange">25</span></span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> permit tcp any host 10.81.43.37 eq <span class="highlight-orange">110</span></span>
                                <br>
                                <span class="comment">! CRÍTICO: Permitir PING (ICMP) y lo que consideres general, o te quedarás sin conexión</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> permit ip any any</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-ext-nacl)#</span> exit</span>
                                <br>
                                <span class="comment">! FINALMENTE: ¡Tienes que asignar el Guardia (ACL) a una puerta (Interfaz)!</span>
                                <span class="comment">! Lo aplicamos a la SVI de Servidores por ejemplo:</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> interface vlan 80</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-if)#</span> ip access-group <span class="highlight-cyan">POLITICAS_LIMA</span> out</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-user-secret"></i><span>Configurar SSH (Acceso Remoto Seguro)</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Históricamente, los ingenieros se conectaban por Telnet. Pero Telnet no encripta la comunicación, envía las contraseñas al desnudo. Por eso habilitamos <strong>SSH (Secure Shell)</strong>. Encripta TODO. Y para completar la Política 5, aplicaremos una restricción para que solo la IP de la PC-Admin pueda usar SSH.</p>
                            
                            <div class="code-block">
                                <span class="comment">! PASO A PASO: Habilitar SSH Seguro en Equipos (Ej: CORE_LIMA)</span>
                                <span class="comment">! 1. Definir un dominio (Requisito para generar las llaves)</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> ip domain-name miempresa.com</span>
                                <span class="comment">! 2. Generar las llaves de encriptación RSA (Usa mínimo 1024 bits)</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> crypto key generate rsa</span>
                                <span class="comment">! 3. Crear el usuario que vas a usar para loguearte</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> username admin secret cisco123</span>
                                <span class="comment">! 4. Forzar SSH y apagar Telnet en las líneas virtuales</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> line vty 0 4</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-line)#</span> transport input <span class="highlight-cyan">ssh</span></span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-line)#</span> login local</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-line)#</span> exit</span>
                                <br>
                                <span class="comment">! LA POLÍTICA 5: Bloquear SSH excepto para la PC-Admin (IP: 10.192.11.194)</span>
                                <span class="comment">! Creamos una pequeña ACL estándar</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> ip access-list standard <span class="highlight-cyan">ADMIN_SOLO</span></span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-std-nacl)#</span> permit host 10.192.11.194</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-std-nacl)#</span> deny any</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-std-nacl)#</span> exit</span>
                                <span class="comment">! Y se la enchufamos a la línea VTY usando 'access-class'</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config)#</span> line vty 0 4</span>
                                <span class="code-line"><span class="cli-prompt">CORE_LIMA(config-line)#</span> access-class <span class="highlight-cyan">ADMIN_SOLO</span> in</span>
                            </div>

                            <div class="theory-box">
                                <h4>Para probar el acceso SSH:</h4>
                                <p>Ve a tu PC-Admin > Command Prompt y ejecuta: <strong><span class="highlight-cyan">ssh -l admin [IP del Core]</span></strong>. (Cuidado, es una "L" minúscula, no un uno, que significa "login"). Prueba desde otra PC de Ventas y mira cómo el router te patea la conexión (Connection Refused).</p>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </section>

        <section id="modulo-8" class="module-section">
            <div class="module-header">
                <span class="module-number">08</span>
                <h2 class="module-title">Redes Inalámbricas (WLAN)</h2>
            </div>
            <div class="card">
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-wifi"></i><span>¿Cómo funciona WiFi en Packet Tracer?</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">Según tu <strong>Laboratorio 06</strong>, hay una diferencia GIGANTE entre un <em>Access Point (AP)</em> y un <em>Wireless Router</em>.</p>
                            <ul>
                                <li><strong>Access Point:</strong> Es simplemente un puente, un switch invisible. Trabaja en Capa 2. Convierte el cable en ondas de radio. No hace DHCP, ni enrutamiento. Simplemente extiende la red por el aire.</li>
                                <li><strong>Wireless Router:</strong> Trabaja en Capa 3. Tiene su propio DHCP interno y realiza NAT. Crea una subred totalmente independiente (como los routers de tu casa).</li>
                            </ul>
                            <p class="theory-text">Para el proyecto empresarial, conectaremos <strong>Access Points</strong> a nuestros Switches. ¡Ojo! En Packet Tracer, las Laptops por defecto vienen con puerto Ethernet de cable. Tienes que apagar la laptop, quitarle el puerto Ethernet, y arrastrar el módulo inalámbrico (WPC300N) para que agarre Wi-Fi.</p>
                        </div>
                    </div>
                </div>

                <div class="accordion-item">
                    <button class="accordion-header">
                        <div class="header-left"><i class="fa-solid fa-signal"></i><span>Paso a Paso: Configurar el Access Point</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">La rúbrica indica que debe haber una red para Clientes y otra para Ejecutivos, lo que significa poner dos APs o un AP con dos redes, separadas en distintas VLANs.</p>
                            
                            <div class="theory-box">
                                <h4>Paso a Paso en Packet Tracer</h4>
                                <ol>
                                    <li>Coloca el Access Point (AP-PT) y conéctalo con un cable directo al switch de la Sede.</li>
                                    <li>Asegúrate de que el puerto del Switch que conecta al AP esté configurado como <strong>Modo Acceso</strong> en la VLAN de Wi-Fi.</li>
                                    <li>Haz clic en el AP > Pestaña <strong>Config</strong> > Izquierda: <strong>Port 1</strong>.</li>
                                    <li>En <strong>SSID</strong>, borra "Default" y escribe el nombre de la red (Ej: <code>WiFi_MIEMPRESA_Ejecutivos</code>).</li>
                                    <li>En Authentication, selecciona <strong>WPA2-PSK</strong> (el estándar de seguridad seguro y moderno).</li>
                                    <li>En PSK Pass Phrase, coloca una contraseña fuerte (Ej: <code>cisco123456</code>).</li>
                                    <li>Abre tu Laptop Inalámbrica > Desktop > PC Wireless > Pestaña Connect. Espera que aparezca la señal, conéctate y pon la contraseña. ¡Y espera a que tu DHCP server le asigne una IP automáticamente!</li>
                                </ol>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section id="modulo-9" class="module-section">
            <div class="module-header">
                <span class="module-number">09</span>
                <h2 class="module-title">Solución Cloud y Backups (AWS)</h2>
            </div>
            <div class="card">
                <div class="accordion-item">
                    <button class="accordion-header active">
                        <div class="header-left"><i class="fa-solid fa-cloud"></i><span>Propuesta de Migración a la Nube</span></div>
                        <i class="fa-solid fa-chevron-down accordion-icon"></i>
                    </button>
                    <div class="accordion-content">
                        <div class="accordion-inner">
                            <p class="theory-text">El hito final del proyecto requiere justificar una migración hacia Cloud Computing (La Nube) para reemplazar o mejorar los servicios "On-Premise" (servidores físicos en la oficina) de MIEMPRESA. Elegimos <strong>Amazon Web Services (AWS)</strong> basándonos en tu trabajo de referencia.</p>
                            
                            <table class="data-table">
                                <tr>
                                    <th>Si en la oficina tienes...</th>
                                    <th>En la nube de AWS alquilas...</th>
                                </tr>
                                <tr>
                                    <td>Discos duros y cintas para Backups</td>
                                    <td><strong>Amazon S3 (Simple Storage Service)</strong>. Es seguro, ilimitado y puedes automatizar copias diarias hacia Amazon Glacier (archivo de bajo costo).</td>
                                </tr>
                                <tr>
                                    <td>Servidor Físico WEB y FTP</td>
                                    <td><strong>Amazon EC2</strong>. Servidores virtuales donde pagas solo por los minutos que la máquina está encendida.</td>
                                </tr>
                                <tr>
                                    <td>Router y Firewall Perimetral</td>
                                    <td><strong>AWS VPC, Route Tables y AWS WAF</strong>. Cortafuegos virtuales y grupos de seguridad súper granulados para tu red.</td>
                                </tr>
                            </table>

                            <div class="theory-box">
                                <h4>El argumento estrella para la sustentación (CAPEX vs OPEX):</h4>
                                <p>En lugar de comprar fierros carísimos de una vez que en 5 años serán obsoletos (<strong>CAPEX</strong> - Gasto de Capital), la empresa migra a un modelo de pago-por-uso mensual (<strong>OPEX</strong> - Gasto Operativo) en AWS, obteniendo una durabilidad inalcanzable localmente (99.999999999% en Amazon S3) y olvidándose de pagar el recibo de luz y aire acondicionado para los servidores.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

if __name__ == "__main__":
    with open("c:/Redes_Guia/mod_02.html", "w", encoding="utf-8") as f:
        f.write(gen_mod_02())
    with open("c:/Redes_Guia/mod_03.html", "w", encoding="utf-8") as f:
        f.write(gen_mod_03())
