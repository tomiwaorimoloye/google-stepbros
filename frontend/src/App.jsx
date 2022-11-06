import './App.css';

function App() {
  return (
    <>
      <header>
        <h1 id="title">U Social</h1>
        <a href="#foo" className="link">Login</a>
      </header>

      <main>
        <div className="box info">
          <h1>Find your schedule buddy with just one tap</h1>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Excepteur sint occaecat cupidatat.</p>
        </div>

        <div className="box">
          <div className="box-title">
            <h3>Create Your Account</h3>
          </div>
          <form className="form-page">
            <input type="text" className="input-box" name="" id="" placeholder='Username'/>
            <select className="input-box" name="" id="">
              <option value="">--Please choose a Faculty--</option>
              <option value="AR">Faculty of Arts</option>
              <option value="AU">Augustana Faculty</option>
              <option value="BC">Faculty of Business</option>
              <option value="ED">Faculty of Education</option>
              <option value="EN">Faculty of Engineering</option>
              <option value="GS">Faculty of Graduate Studies and Research</option>
              <option value="LA">Faculty of Law</option>
              <option value="MH">Faculty of Medicine and Dentistry</option>
              <option value="NS">Faculty of Native Studies</option>
              <option value="NU">Facuylty of Nursing</option>
              <option value="PE">Faculty of Kinesiology, Sport, and REcreation</option>
              <option value="PH">Faculty of Pharmacy and Pharmaceutical Sciences</option>
              <option value="PS">School of Public Health</option>
              <option value="RM">Faculty of Rehabilitaion Medicine</option>
              <option value="SA">Faculté Saint-Jean</option>
              <option value="SC">Faculty of Science</option>
              <option value="SS">St Stephen's College</option>
            </select>
            <input type="password" className="input-box" name="" id="" placeholder='Password'/>
            <input type="password" className="input-box" name="" id="" placeholder='Confirm password'/>
            <button className="btn  input-boxprimary-btn">Sign Up</button>
          </form>
        </div>
      </main>

      <footer>
      </footer>
    </>
  );
}

export default App