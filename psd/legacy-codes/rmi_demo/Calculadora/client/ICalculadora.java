import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ICalculadora extends Remote {
	
	float soma(float a, float b) throws RemoteException;
	float subtracao(float a, float b) throws RemoteException;
	float multiplicacao(float a, float b) throws RemoteException;
	float divisao(float a, float b) throws RemoteException;

}
