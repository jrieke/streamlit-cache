import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection
} from "streamlit-component-lib";
import { ReactNode } from "react"
import Cookies from 'universal-cookie';
import { v4 as uuidv4 } from 'uuid';

// interface State {
//   numClicks: number
// }

const cookies = new Cookies();

/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
class UserIdComponent extends StreamlitComponentBase {
  // public state = { numClicks: 0 }

  public render = (): ReactNode => {
    // Arguments that are passed to the plugin in Python are accessible
    // via `this.props.args`. Here, we access the "name" arg.
    // const name = this.props.args["name"]

    // Show a button and some text.
    // When the button is clicked, we'll increment our "numClicks" state
    // variable, and send its new value back to Streamlit, where it'll
    // be available to the Python program.
    // return (
    //   <span>
    //     Hello, {name}! &nbsp;
    //     <button onClick={this.onClicked} disabled={this.props.disabled}>
    //       Click Me!
    //     </button>
    //   </span>
    // )
    return (null);
  }

  public componentDidMount() {
    
    // Check for existing user id in cookies.
    var user_id = cookies.get('streamlit_user_id')
    if (user_id) {
      console.log("[Streamlit] Found existing user id: " + user_id)
    } else {
      // Create new random user id.
      user_id = uuidv4()

      // Set cookie expiry date one year from now.
      var inOneYear = new Date();
      inOneYear.setFullYear(inOneYear.getFullYear() + 1)

      // Store new user id in cookie.
      cookies.set('streamlit_user_id', user_id, { path: '/', expires: inOneYear })
      cookies.set('streamlit_user_id', user_id, { path: '/' , expires: inOneYear, domain: "share.streamlit.io"})
      console.log("[Streamlit] Couldn't find existing user id, storing new one: " + user_id)
    }

    // Return user id to Streamlit, so we can read it in Python.
    Streamlit.setComponentValue(user_id);

  }

  /** Click handler for our "Click Me!" button. */
  // private onClicked = (): void => {
  //   // Increment state.numClicks, and pass the new value back to
  //   // Streamlit via `Streamlit.setComponentValue`.
  //   // this.setState(
  //   //   prevState => ({ numClicks: prevState.numClicks + 1 }),
  //   //   () => Streamlit.setComponentValue(this.state.numClicks)
  //   // )


    
  // }
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(UserIdComponent)
