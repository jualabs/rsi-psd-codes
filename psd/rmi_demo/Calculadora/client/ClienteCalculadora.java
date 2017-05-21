import java.rmi.Naming;
import java.rmi.RemoteException;

public class ClienteCalculadora {
	
	public static void main(String[] args) {
		
		ICalculadora rCalculadora = null;
		
		try {
			String objname =  "rmi://localhost/servidor_calculadora";
			System.out.println("Procurando pelo objeto " + objname);
			rCalculadora = (ICalculadora) Naming.lookup(objname);
		}
		catch (Exception e) {
			System.err.println("Problemas ao executar o lookup! " + e);
			e.printStackTrace();
			System.exit(2);
		}
		try {
			float valorRetorno = 0.0f;
			valorRetorno = rCalculadora.soma(14, 14);
			System.out.println("soma de 14 + 14 = " + valorRetorno);
			valorRetorno = rCalculadora.subtracao(14, 14);
			System.out.println("subtracao de 14 - 14 = " + valorRetorno);
			valorRetorno = rCalculadora.multiplicacao(14, 2);
			System.out.println("multiplicacao de 14 * 2 = " + valorRetorno);
			valorRetorno = rCalculadora.divisao(14, 2);
			System.out.println("divisao de 14 / 2 = " + valorRetorno);
		}
		catch (RemoteException re) {
			System.err.println("Problemas durante chamada remota! " + re);
			re.printStackTrace();
			System.exit(3);
		}
	}
}
