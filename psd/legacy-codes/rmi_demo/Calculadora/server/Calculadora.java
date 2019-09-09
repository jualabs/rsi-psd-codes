import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class Calculadora extends UnicastRemoteObject implements ICalculadora {
	private static final long serialVersionUID = 1L;
	
	public Calculadora() throws RemoteException {
	}
	
	public float soma(float a, float b) {
		System.out.println("somou");
		return (a + b);
	}
	public float subtracao(float a, float b) {
		System.out.println("subtraiu");
		return (a - b);
	}
	public float multiplicacao(float a, float b) {
		System.out.println("multiplicou");
		return (a * b);
	}
	public float divisao(float a, float b) {
		System.out.println("dividiu");
		return (a / b);
	}

}
