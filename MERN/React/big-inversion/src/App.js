import logo from './logo.svg';
import './App.css';

import PersonCard from './components/PersonCard';

function App() {
  return (
    <div>
      <PersonCard lastName = "Doe" firstName = "Jane" age = { 45 } color = "Black" />
      <PersonCard lastName = "Smith" firstName = "John" age = { 88 } color = "Brown" />
      <PersonCard lastName = "Fillmore" firstName = "Millard" age = { 50 } color = "Brown" />
      <PersonCard lastName = "Smith" firstName = "Maria" age = { 62 } color = "Brown" />
    </div>
  );
}

export default App;
