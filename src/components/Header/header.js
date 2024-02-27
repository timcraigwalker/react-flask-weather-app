import "./header.css"

const Header = () => {
    const logout = () => {
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        };
        return fetch('/auth/logout', requestOptions)
    }

    return (
        <div className="header">
            <div className="title">Weather App</div>
            <div className="account-icon">
                <button onClick={logout}>Logout</button>
            </div>
        </div>
    )
}

export default Header;