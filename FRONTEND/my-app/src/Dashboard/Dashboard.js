
import React, { useState } from 'react';
import './Dashboard.css';
function Dashboard() {
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };

  return (
    <div className="dashboard-container">
      <div className="sidebar">
        <div className="user-info">Usuario</div>
        <button className="sidebar-button">Asistencia</button>
        <button className="sidebar-button">Pago</button>
        <button className="sidebar-button">Registro (Alimentos)</button>
      </div>
      <div className="content">
        <div className="settings" onClick={toggleMenu}>
          Configuraciones
          {menuOpen && (
            <div className="dropdown-menu">
              <button className="dropdown-item">Ver Reglamento</button>
              <button className="dropdown-item">Cerrar sesión</button>
              <button className="dropdown-item">Verificar calendario</button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
 export { Dashboard }